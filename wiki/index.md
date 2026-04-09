# GEO RNA-seq Dataset Index

> Auto-generated index of RNA-sequencing datasets from NCBI GEO.
> Covers publications from **2026/01/09 – 2026/04/08** (5,580 datasets).

## Search

For specific queries (e.g., "bulk RNA-seq from 5XFAD mouse brain"), grep the search index:

```
grep -i "5xfad" wiki/search_index.txt
```

Format: `accession|modality|organism|n_samples|suppfiles|topics|title|keywords`

See [search_index.txt](search_index.txt) (5,580 entries, one per dataset).

## By Sequencing Modality

| Modality | Count | Page |
|----------|------:|------|
| Bulk RNA-seq | 3,677 | [bulk_rnaseq.md](assays/bulk_rnaseq.md) |
| Single-cell RNA-seq | 1,441 | [scrna_seq.md](assays/scrna_seq.md) |
| Single-nucleus RNA-seq | 365 | [snrna_seq.md](assays/snrna_seq.md) |
| Spatial Transcriptomics | 97 | [spatial.md](assays/spatial.md) |

## By Research Topic

| Topic | Count | Page |
|-------|------:|------|
| Development & Differentiation | 9,255 | [development.md](topics/development.md) |
| Cancer | 8,808 | [cancer.md](topics/cancer.md) |
| Immunology | 8,767 | [immunology.md](topics/immunology.md) |
| Metabolism & Metabolic Disease | 4,904 | [metabolism.md](topics/metabolism.md) |
| Neuroscience | 4,433 | [neuroscience.md](topics/neuroscience.md) |
| Infectious Disease | 4,213 | [infectious_disease.md](topics/infectious_disease.md) |
| Drug Response & Pharmacology | 3,613 | [drug_response.md](topics/drug_response.md) |
| Epigenetics & Chromatin | 3,319 | [epigenetics.md](topics/epigenetics.md) |
| Cardiovascular | 2,486 | [cardiovascular.md](topics/cardiovascular.md) |
| Muscle & Musculoskeletal | 2,357 | [skeletal_muscle.md](topics/skeletal_muscle.md) |
| Hematopoiesis & Blood | 2,289 | [hematopoiesis.md](topics/hematopoiesis.md) |
| Fibrosis & Wound Healing | 1,834 | [fibrosis_wound.md](topics/fibrosis_wound.md) |
| Lung & Respiratory | 1,813 | [lung_respiratory.md](topics/lung_respiratory.md) |
| Plant Biology | 1,706 | [plant_biology.md](topics/plant_biology.md) |
| Aging & Senescence | 1,644 | [aging.md](topics/aging.md) |
| CRISPR & Gene Editing | 1,639 | [crispr_gene_editing.md](topics/crispr_gene_editing.md) |
| Kidney & Renal | 1,484 | [kidney.md](topics/kidney.md) |
| Reproductive Biology | 1,452 | [reproduction.md](topics/reproduction.md) |
| Gut & Intestinal Biology | 1,428 | [gut_intestine.md](topics/gut_intestine.md) |
| Skin & Dermatology | 901 | [skin.md](topics/skin.md) |

## By Organism

| Organism | Count | Page |
|----------|------:|------|
| Homo sapiens | 2,330 | [homo_sapiens.md](organisms/homo_sapiens.md) |
| Mus musculus | 2,235 | [mus_musculus.md](organisms/mus_musculus.md) |

## Data Availability Overview

**Important caveat:** GEO's `suppFile` field lists file extensions found *inside* supplementary archives, not individually downloadable files. The actual download is typically a single TAR/gz bundle from the FTP link. For example, "MTX, TSV" means the archive contains sparse matrix and barcode/feature files (standard 10x CellRanger output), not that these are separate downloads.

Supplementary file types across all RNA-seq datasets (indicates what preprocessed data is available beyond raw FASTQ):

| File Type | Bulk | scRNA | snRNA | Spatial | Notes |
|-----------|-----:|------:|------:|--------:|-------|
| TXT | 1,784 | 269 | 231 | 19 | Often count matrices or gene lists |
| CSV | 745 | 292 | 22 | 27 | Count matrices, DE results |
| TSV | 362 | 840 | 81 | 40 | Barcodes, features, metadata (10x format) |
| XLSX | 529 | 48 | — | — | DE results, sample metadata |
| MTX | — | 775 | 68 | 33 | Sparse count matrices (10x CellRanger) |
| H5/H5AD | — | 268 | 40 | 23 | AnnData/CellRanger HDF5 objects |
| RDS | — | 127 | 17 | 12 | R objects (Seurat, SCE) |
| BW/BIGWIG | 266 | 28 | 5 | — | Coverage tracks |

## Log

See [log.md](log.md) for ingest history.
