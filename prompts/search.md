# Search GEO Datasets

Use this prompt to find GEO datasets matching a natural-language query.

## Process

1. **Parse the query** — identify organism, assay type, research topic, sample count requirements, file format preferences, and domain-specific terms (mouse model names, project names, cell types, histone marks, etc.).

2. **Choose the right shard** based on assay type:
   - RNA-seq (bulk / scRNA / snRNA / spatial) → `wiki/search_index_rnaseq.txt`
   - ChIP-seq → `wiki/search_index_chipseq.txt`
   - ATAC-seq → `wiki/search_index_atacseq.txt`
   - CUT&RUN / CUT&Tag → `wiki/search_index_cut_run_tag.txt`
   - Methylation (WGBS/RRBS/array) → `wiki/search_index_methylation.txt`
   - Multiomics (CITE-seq / 10x Multiome / SHARE-seq) → `wiki/search_index_multiomics.txt`
   - Unknown or cross-assay → start with `wiki/search_index_rnaseq.txt`, expand as needed

3. **Grep the shard** with relevant terms (case-insensitive). Format:
   `accession|modality|organism|n_samples|files|topics|title|keywords|flags`
   - Try organism name, modality, topic keywords, and domain terms separately, then intersect
   - `flags` column (9th): `multiomics` = paired multi-assay data exists for this record

4. **Return a ranked results table**: accession, title, organism, modality, n_samples, files. Note why each matches.

5. **For top 3–5 hits**, explain the match quality — does it satisfy all constraints? Any caveats?

6. **File format guidance** — if the user might want to download data, point to the relevant protocol:
   - `.rds.gz` → `wiki/protocols/rds_seurat.md`
   - `.h5ad.gz` → `wiki/protocols/h5ad_anndata.md`
   - `.h5` (CellRanger) → `wiki/protocols/h5_cellranger.md`
   - `.mtx.gz` → `wiki/protocols/mtx_10x.md`
   - `.csv.gz` / `.tsv.gz` (bulk) → `wiki/protocols/csv_tsv_counts.md`
   - `no_suppl` / SRA → `wiki/protocols/fastq_alignment.md`
