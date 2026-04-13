# FASTQ / SRA — Raw Reads

**Effort: ⭐⭐⭐⭐ Hard | Time: 1–3 days**

When a GEO dataset has no supplementary files (or only a `RAW.tar` with unprocessed reads), the processed data lives on SRA and you'll need to download FASTQ files and run an alignment pipeline yourself. This is the most involved path but gives you full control over preprocessing choices.

## Requirements

| | |
|---|---|
| **OS** | **Linux strongly recommended.** STAR, featureCounts, and CellRanger are Linux-native. Mac (Intel or Apple Silicon via Rosetta/conda) works but is slower. Windows is not supported — use WSL2, a Linux VM, or a cloud instance. |
| **Compute** | **Cluster or high-core workstation required.** Index building needs 32–64 GB RAM; alignment is CPU-bound. A 16-core node finishes one sample in 30–60 min. A laptop will work for small datasets but takes hours per sample. |
| **RAM** | **STAR genome index: 30–35 GB for human/mouse (GRCh38/mm10). Keep at least 32 GB free during alignment.** featureCounts adds ~2–4 GB. CellRanger needs 64 GB for 10x data. |
| **Storage** | **Plan for 5–30 GB per sample in FASTQ** (paired-end, compressed). BAM files add 2–10 GB per sample. STAR index is ~28 GB on disk. Budget ~2× your FASTQ total for intermediate files. |
| **Key tools** | `sra-tools` (fasterq-dump), `STAR`, `subread/featureCounts`, `CellRanger` (10x); optional `trimmomatic` or `fastp` for adapter trimming |

> **Linux note:** all tools install cleanly via conda (`bioconda` channel). On a cluster, load modules with `module load star featurecounts sra-tools` or use a conda environment in your `$HOME`.

> **Mac note:** STAR runs on Mac but is slower. Apple Silicon (M1/M2/M3) requires Intel emulation via Rosetta for some bioinformatics tools — install x86_64 conda environment explicitly if needed.

> **Windows WSL2:** install Ubuntu via WSL2, then follow Linux instructions. Performance is close to native Linux for CPU-bound tools.

---

## When you're in this situation

- The FTP listing shows only `RAW.tar`, no count matrices
- The files column in the search index says `no_suppl` or only BAM/FASTQ files
- The GEO page links to an SRA accession but no processed supplementary files

Check the GEO page's "Relations" section — SRA accessions are listed as `SRX...` (experiment) or `SRP...` (project) links.

---

## Steps

### Step 1 — Set up the environment *(first time only, ~20–40 min)*

```bash
# Install sra-tools and alignment tools via conda (bioconda channel)
conda create -n alignment -c bioconda -c conda-forge \
    sra-tools star subread fastp -y
conda activate alignment

# Verify
fasterq-dump --version
STAR --version
featureCounts -v
```

> **Cluster:** on most HPC systems, tools are available as modules (`module load star`). Check with your sysadmin. If you need a specific version, a conda environment in `$HOME` is portable.

### Step 2 — Find SRR accessions for your GEO dataset *(~10–20 min)*

```python
# Quick lookup using NCBI E-utilities
import urllib.request, json

def get_srr_for_gse(gse_accession):
    """Get SRA run accessions for a GEO series."""
    url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
           f"?db=sra&term={gse_accession}&retmode=json&retmax=1000")
    with urllib.request.urlopen(url) as r:
        ids = json.load(r)["esearchresult"]["idlist"]

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

Or use the [SRA Run Selector](https://www.ncbi.nlm.nih.gov/Traces/study/) — paste the GSE or SRP accession to get a full table of SRR IDs as a downloadable CSV.

### Step 3 — Download FASTQ files from SRA *(~30 min – several hours per sample)*

```bash
# fasterq-dump is the modern, faster replacement for fastq-dump
fasterq-dump SRR12345678 --split-files --outdir fastq/ --threads 8

# For paired-end data this produces:
# SRR12345678_1.fastq  (R1)
# SRR12345678_2.fastq  (R2)

# Compress output (~2–5 min per sample)
gzip fastq/SRR12345678_*.fastq

# Download multiple runs from a list
cat SRR_Acc_List.txt | while read srr; do
    fasterq-dump $srr --split-files --outdir fastq/ --threads 8
    gzip fastq/${srr}*.fastq
done
```

> **Download speed:** NCBI bandwidth is often 10–30 MB/s. A 10 GB FASTQ (typical paired-end RNA-seq sample) takes 5–15 min. For many samples or large datasets, consider [AWS Open Data](https://registry.opendata.aws/ncbi-sra/) or [Google Cloud SRA](https://www.ncbi.nlm.nih.gov/sra/docs/sra-google-cloud/) — SRA data is available in cloud buckets for free egress.

> **Storage warning:** always check available disk space before downloading. A 50-sample dataset at 5 GB/sample = 250 GB.

### Step 4A — Bulk RNA-seq: build STAR genome index *(~30–60 min; do once, reuse)*

```bash
# Download genome and annotation (example: human GRCh38)
wget https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
wget https://ftp.ensembl.org/pub/release-110/gtf/homo_sapiens/Homo_sapiens.GRCh38.110.gtf.gz
gunzip *.gz

# Build STAR genome index — needs ~32 GB RAM; takes 30–60 min
STAR --runMode genomeGenerate \
     --genomeDir star_index/ \
     --genomeFastaFiles Homo_sapiens.GRCh38.dna.primary_assembly.fa \
     --sjdbGTFfile Homo_sapiens.GRCh38.110.gtf \
     --runThreadN 16
```

> **SLURM job script for index building:**
> ```bash
> #!/bin/bash
> #SBATCH --job-name=star_index
> #SBATCH --cpus-per-task=16
> #SBATCH --mem=64G
> #SBATCH --time=02:00:00
>
> conda activate alignment
> STAR --runMode genomeGenerate \
>      --genomeDir star_index/ \
>      --genomeFastaFiles Homo_sapiens.GRCh38.dna.primary_assembly.fa \
>      --sjdbGTFfile Homo_sapiens.GRCh38.110.gtf \
>      --runThreadN 16
> ```

### Step 4B — Bulk RNA-seq: align each sample *(~30–60 min per sample on 16 cores)*

```bash
# Align each sample (paired-end example)
STAR --runMode alignReads \
     --genomeDir star_index/ \
     --readFilesIn fastq/SRR12345678_1.fastq.gz fastq/SRR12345678_2.fastq.gz \
     --readFilesCommand zcat \
     --outSAMtype BAM SortedByCoordinate \
     --outSAMattributes NH HI AS NM \
     --outFileNamePrefix bam/SRR12345678_ \
     --runThreadN 16

# Count reads per gene (all samples at once — fast, ~5–15 min)
featureCounts -T 16 \
              -a Homo_sapiens.GRCh38.110.gtf \
              -o counts/all_samples_counts.txt \
              bam/*.bam
```

> **SLURM array job for aligning all samples:**
> ```bash
> #!/bin/bash
> #SBATCH --job-name=star_align
> #SBATCH --cpus-per-task=16
> #SBATCH --mem=40G
> #SBATCH --time=02:00:00
> #SBATCH --array=1-50%10   # 50 samples, 10 at a time
>
> SRR=$(sed -n "${SLURM_ARRAY_TASK_ID}p" SRR_Acc_List.txt)
> conda activate alignment
> STAR --runMode alignReads \
>      --genomeDir star_index/ \
>      --readFilesIn fastq/${SRR}_1.fastq.gz fastq/${SRR}_2.fastq.gz \
>      --readFilesCommand zcat \
>      --outSAMtype BAM SortedByCoordinate \
>      --outFileNamePrefix bam/${SRR}_ \
>      --runThreadN 16
> ```

### Step 4C — Bulk RNA-seq: downstream analysis in R *(~30 min – 2 hours; laptop fine)*

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

> **OS note:** DESeq2 runs on Mac and Windows without issues. This is the step where a laptop is fine — the heavy computation is already done on the cluster.

### Step 5A — Single-cell RNA-seq: STARsolo *(~30–60 min per sample on 16 cores)*

STARsolo is open-source and faster than CellRanger. Use the same genome index built in Step 4A.

```bash
# 10x Chromium v3 chemistry (most datasets 2019+)
STAR --runMode alignReads \
     --genomeDir star_index/ \
     --readFilesIn fastq/SRR_R2.fastq.gz fastq/SRR_R1.fastq.gz \
     --readFilesCommand zcat \
     --soloType CB_UMI_Simple \
     --soloCBwhitelist 3M-february-2018.txt \
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

> **Read order:** for 10x data, R1 is the barcode+UMI read and R2 is the cDNA. STARsolo expects `--readFilesIn R2 R1` (cDNA first). Getting this backwards produces zero valid barcodes.

### Step 5B — Single-cell RNA-seq: CellRanger *(~1–3 hours per sample; needs 64 GB RAM)*

```bash
# Download CellRanger from: https://www.10xgenomics.com/support/software/cell-ranger
# Download pre-built reference genome from 10x
wget https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-GRCh38-2020-A.tar.gz
tar -xf refdata-gex-GRCh38-2020-A.tar.gz

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

> **SLURM for CellRanger:**
> ```bash
> #!/bin/bash
> #SBATCH --job-name=cellranger
> #SBATCH --cpus-per-task=16
> #SBATCH --mem=128G
> #SBATCH --time=08:00:00
>
> cellranger count --id=$SAMPLE \
>     --transcriptome=refdata-gex-GRCh38-2020-A \
>     --fastqs=fastq/ --sample=$SAMPLE \
>     --localcores=16 --localmem=64
> ```

### Step 5C — Spatial transcriptomics: CellRanger Visium *(~2–4 hours per sample)*

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

---

## Checking whether processed data exists before downloading FASTQ

Before committing to the alignment pipeline, always check — most authors deposit processed data too:

1. The GEO FTP listing (in the search index `files` column)
2. The Processed Data section of the GEO accession page
3. The SRA page itself — some authors upload processed matrices as SRA supplementary files

Many datasets that appear to have no supplements actually do — they're just not visible in the standard GEO view.

---

## Common pitfalls

- **Read order for single-cell:** for 10x data, R1 contains the cell barcode + UMI and R2 contains the cDNA. STARsolo expects `--readFilesIn R2 R1` (cDNA first). Getting this backwards produces zero valid barcodes.
- **Chemistry version:** 10x v2 uses a 16 bp barcode + 10 bp UMI; v3 uses 16 bp + 12 bp. Using the wrong whitelist or UMI length causes poor mapping. The GEO page usually lists the library prep kit.
- **Genome/annotation version mismatch:** use the same genome assembly and GTF version throughout. Mixing GRCh37 and GRCh38 gene coordinates causes catastrophic alignment failures.
- **Multi-mapper reads:** STAR by default keeps only uniquely mapped reads for gene counting. This is usually fine for mRNA-seq but may matter for repetitive elements.
- **SRA download speed:** `fasterq-dump` is much faster than `fastq-dump` but still limited by NCBI bandwidth. For large projects, consider [AWS Open Data](https://registry.opendata.aws/ncbi-sra/) or [Google Cloud SRA](https://www.ncbi.nlm.nih.gov/sra/docs/sra-google-cloud/) — SRA data is available in cloud buckets for free egress.
- **Disk space mid-run:** STAR writes temporary files that can be 2–3× the BAM size. Check free space before starting a large batch. Use `--outTmpDir` to redirect temp files to a scratch partition if needed.
- **Windows:** STAR and CellRanger do not run on Windows natively. Use WSL2, a Linux VM, or a cloud instance (AWS `c6i.4xlarge` — 16 cores, 32 GB RAM — is ~$0.68/hr).
