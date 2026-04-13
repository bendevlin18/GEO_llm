# FASTQ / SRA — Raw Reads

**Effort: ⭐⭐⭐⭐ Hard | Time: 1–3 days**

When a GEO dataset has no supplementary files (or only a `RAW.tar` with unprocessed reads), the processed data lives on SRA and you'll need to download FASTQ files and run an alignment pipeline yourself. This is the most involved path but gives you full control over preprocessing choices.

## When you're in this situation

- The FTP listing shows only `RAW.tar`, no count matrices
- The files column in the search index says `no_suppl` or only BAM/FASTQ files
- The GEO page links to an SRA accession but no processed supplementary files

Check the GEO page's "Relations" section — SRA accessions are listed as `SRX...` (experiment) or `SRP...` (project) links.

## Step 1 — Download from SRA

```bash
# Install sra-tools (conda recommended)
conda install -c bioconda sra-tools -y

# Download a single run (SRR accession) as FASTQ
# fasterq-dump is the modern, faster replacement for fastq-dump
fasterq-dump SRR12345678 --split-files --outdir fastq/ --threads 8

# For paired-end data, this produces:
# SRR12345678_1.fastq  (R1)
# SRR12345678_2.fastq  (R2)

# Compress output
gzip fastq/SRR12345678_*.fastq

# Download multiple runs for a project
# Get the SRR list from: https://www.ncbi.nlm.nih.gov/Traces/study/?acc=SRP...
# Or use the SRA Run Selector: https://www.ncbi.nlm.nih.gov/Traces/study/
cat SRR_Acc_List.txt | while read srr; do
    fasterq-dump $srr --split-files --outdir fastq/ --threads 8
    gzip fastq/${srr}*.fastq
done
```

## Step 2A — Bulk RNA-seq alignment (STAR + featureCounts)

```bash
# Download genome and annotation (example: human GRCh38)
wget https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
wget https://ftp.ensembl.org/pub/release-110/gtf/homo_sapiens/Homo_sapiens.GRCh38.110.gtf.gz
gunzip *.gz

# Build STAR genome index (do once, reuse for all samples)
STAR --runMode genomeGenerate \
     --genomeDir star_index/ \
     --genomeFastaFiles Homo_sapiens.GRCh38.dna.primary_assembly.fa \
     --sjdbGTFfile Homo_sapiens.GRCh38.110.gtf \
     --runThreadN 16

# Align each sample (paired-end example)
STAR --runMode alignReads \
     --genomeDir star_index/ \
     --readFilesIn fastq/SRR12345678_1.fastq.gz fastq/SRR12345678_2.fastq.gz \
     --readFilesCommand zcat \
     --outSAMtype BAM SortedByCoordinate \
     --outSAMattributes NH HI AS NM \
     --outFileNamePrefix bam/SRR12345678_ \
     --runThreadN 16

# Count reads per gene
featureCounts -T 16 \
              -a Homo_sapiens.GRCh38.110.gtf \
              -o counts/all_samples_counts.txt \
              bam/*.bam
```

### Downstream in R

```r
library(DESeq2)

# Read featureCounts output
counts_raw <- read.table("counts/all_samples_counts.txt",
                          header = TRUE, row.names = 1, skip = 1)
counts <- counts_raw[, 6:ncol(counts_raw)]   # drop metadata cols

# Rename columns to sample IDs
colnames(counts) <- gsub("bam/(.*?)_Aligned.*", "\\1", colnames(counts))

# Build DESeq2 object and run
coldata <- data.frame(condition = factor(c("ctrl","ctrl","treat","treat")),
                      row.names = colnames(counts))
dds <- DESeqDataSetFromMatrix(counts, coldata, ~condition)
dds <- DESeq(dds)
res <- results(dds)
```

## Step 2B — Single-cell RNA-seq alignment (STARsolo or CellRanger)

### STARsolo (open source, faster)

```bash
# Build STAR index as above, then:

# 10x Chromium v3 chemistry (most datasets 2019+)
STAR --runMode alignReads \
     --genomeDir star_index/ \
     --readFilesIn fastq/SRR_R2.fastq.gz fastq/SRR_R1.fastq.gz \
     --readFilesCommand zcat \
     --soloType CB_UMI_Simple \
     --soloCBwhitelist 3M-february-2018.txt \   # 10x v3 whitelist
     --soloCBstart 1 --soloCBlen 16 \
     --soloUMIstart 17 --soloUMIlen 12 \
     --outSAMtype BAM SortedByCoordinate \
     --outSAMattributes NH HI nM AS CR UR CB UB GX GN sS sQ sM \
     --outFileNamePrefix starsolo_out/ \
     --runThreadN 16

# Output: starsolo_out/Solo.out/Gene/filtered/
# Contains: barcodes.tsv, features.tsv, matrix.mtx
# Load into Seurat or scanpy as per the MTX protocol
```

### CellRanger (10x official, requires license-free download)

```bash
# Download CellRanger from: https://www.10xgenomics.com/support/software/cell-ranger

# Download reference genome (pre-built by 10x)
wget https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz

cellranger count \
    --id=sample_name \
    --transcriptome=refdata-gex-GRCh38-2020-A \
    --fastqs=fastq/ \
    --sample=SRR12345678 \
    --localcores=16 \
    --localmem=64

# Output: sample_name/outs/filtered_feature_bc_matrix.h5
# Load as per the H5 protocol
```

## Step 2C — Spatial transcriptomics (10x Visium)

```bash
# Visium requires both FASTQ and a tissue image
cellranger-spatial count \
    --id=visium_sample \
    --transcriptome=refdata-gex-GRCh38-2020-A \
    --fastqs=fastq/ \
    --image=tissue_hires_image.tif \
    --slide=V10J25-109 \
    --area=A1 \
    --localcores=16

# Output includes:
# filtered_feature_bc_matrix.h5
# spatial/ directory with tissue positions, scalefactors
```

## Finding SRR accessions for a GEO dataset

```python
# Quick lookup using NCBI E-utilities
import urllib.request, json

def get_srr_for_gse(gse_accession):
    """Get SRA run accessions for a GEO series."""
    # Step 1: GSE → SRA study accession
    url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
           f"?db=sra&term={gse_accession}&retmode=json&retmax=1000")
    with urllib.request.urlopen(url) as r:
        ids = json.load(r)["esearchresult"]["idlist"]

    # Step 2: SRA IDs → run accessions
    runs = []
    for uid in ids[:5]:   # sample first 5
        url2 = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
                f"?db=sra&id={uid}&retmode=xml")
        with urllib.request.urlopen(url2) as r:
            xml = r.read().decode()
        import re
        runs += re.findall(r'<Run accession="(SRR\d+)"', xml)
    return runs

srr_list = get_srr_for_gse("GSE115931")
print(srr_list[:5])
```

Or use the [SRA Run Selector](https://www.ncbi.nlm.nih.gov/Traces/study/) — paste the GSE or SRP accession to get a table of all SRR IDs you can download.

## Checking whether processed data exists before downloading FASTQ

Before committing to the alignment pipeline, always check:

1. The GEO FTP listing (in the search index `files` column)
2. The Processed Data section of the GEO accession page
3. The SRA page itself — some authors upload processed matrices as SRA supplementary files

Many datasets that appear to have no supplements actually do — they're just not visible in the standard GEO view.

## Common pitfalls

- **Read order for single-cell:** for 10x data, R1 contains the cell barcode + UMI and R2 contains the cDNA. STARsolo expects `--readFilesIn R2 R1` (cDNA first). Getting this backwards produces zero valid barcodes.
- **Chemistry version:** 10x v2 uses a 16 bp barcode + 10 bp UMI; v3 uses 16 bp + 12 bp. Using the wrong whitelist or UMI length causes poor mapping. The GEO page usually lists the library prep kit.
- **Genome/annotation version mismatch:** use the same genome assembly and GTF version throughout. Mixing GRCh37 and GRCh38 gene coordinates causes catastrophic alignment failures.
- **Multi-mapper reads:** STAR by default keeps only uniquely mapped reads for gene counting. This is usually fine for mRNA-seq but may matter for repetitive elements.
- **SRA download speed:** `fasterq-dump` is much faster than `fastq-dump` but still limited by NCBI bandwidth. For large projects, consider [AWS Open Data](https://registry.opendata.aws/ncbi-sra/) or [Google Cloud SRA](https://www.ncbi.nlm.nih.gov/sra/docs/sra-google-cloud/) — SRA data is available in cloud buckets for free egress.
