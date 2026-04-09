"""
Tag RNA-seq datasets with research topics based on title + summary.
Multi-label: a dataset can belong to multiple topics.
"""
import json
import re
from collections import Counter, defaultdict


# Topic taxonomy: topic_key -> (display_name, keywords)
# Keywords are matched against lowercased title + summary.
# Order matters within a topic (first match wins), but a record can match multiple topics.
TOPICS = {
    "cancer": (
        "Cancer",
        [
            "cancer", "tumor", "tumour", "carcinoma", "melanoma", "leukemia",
            "leukaemia", "lymphoma", "glioblastoma", "glioma", "sarcoma",
            "myeloma", "neuroblastoma", "mesothelioma", "oncogen", "metastas",
            "neoplasm", "malignant", "chemoresist", "anti-tumor", "anti-tumour",
            "tumor microenvironment", "tme", "car t", "car-t",
            "hepatocellular", "pancreatic ductal", "nsclc", "breast cancer",
            "lung cancer", "colorectal cancer", "prostate cancer", "ovarian cancer",
            "aml", "cll", "dlbcl", "acute myeloid",
        ],
    ),
    "immunology": (
        "Immunology",
        [
            "immune", "immunity", "immunolog", "t cell", "t-cell", "b cell",
            "b-cell", "macrophage", "dendritic cell", "nk cell", "natural killer",
            "cytokine", "chemokine", "inflammat", "autoimmun", "allerg",
            "interferon", "interleukin", "lymphocyte", "monocyte", "neutrophil",
            "eosinophil", "mast cell", "antibod", "immunoglobulin",
            "antigen", "mhc", "hla", "toll-like", "innate immun",
            "adaptive immun", "thymus", "thymocyte", "germinal center",
            "regulatory t", "treg", "th1", "th2", "th17",
        ],
    ),
    "neuroscience": (
        "Neuroscience",
        [
            "neuron", "neural", "brain", "cortex", "cortical", "hippocamp",
            "cerebr", "cerebell", "astrocyte", "microglia", "oligodendrocyte",
            "synap", "axon", "dendrit", "neurodegen", "alzheimer",
            "parkinson", "huntington", "amyotrophic", "multiple sclerosis",
            "epilep", "glia", "neuroinflam", "spinal cord", "retina",
            "retinal", "dopamin", "serotonin", "glutamat", "gaba",
            "neuropsych", "cognit", "thalamus", "hypothalamus", "striatum",
            "amygdala", "prefrontal", "motor cortex", "sensory cortex",
        ],
    ),
    "development": (
        "Development & Differentiation",
        [
            "embryo", "embryonic", "develop", "differentiat", "morphogen",
            "organogen", "gastrulat", "somit", "limb bud", "neural crest",
            "mesoderm", "endoderm", "ectoderm", "pluripoten", "totipoten",
            "stem cell", "progenitor", "lineage", "fate", "reprogramm",
            "ips cell", "ipsc", "hesc", "organoid", "blastocyst",
            "zygot", "oocyte", "spermat", "gametogen", "fetal",
            "foetal", "neonatal", "postnatal",
        ],
    ),
    "cardiovascular": (
        "Cardiovascular",
        [
            "heart", "cardiac", "cardiomyocyte", "myocardial", "vascular",
            "endotheli", "atheroscl", "artery", "arterial", "aorta",
            "coronary", "angiogen", "vasculat", "hypertens", "thrombo",
            "platelet", "blood vessel", "ventricular", "atrial",
            "heart failure", "cardiomyopathy", "valve", "pericardi",
        ],
    ),
    "metabolism": (
        "Metabolism & Metabolic Disease",
        [
            "metabol", "diabetes", "diabetic", "insulin", "glucose",
            "lipid", "adipocyte", "adipose", "obesity", "obese",
            "cholesterol", "fatty acid", "mitochondri", "glycoly",
            "oxidative phosphoryl", "krebs", "tca cycle", "beta cell",
            "islet", "hepatocyte", "liver", "hepatic", "steatosis",
            "nafld", "nash",
        ],
    ),
    "epigenetics": (
        "Epigenetics & Chromatin",
        [
            "epigenet", "chromatin", "histone", "methylation", "acetylat",
            "enhancer", "promoter", "silenc", "imprint", "polycomb",
            "trithorax", "chip-seq", "atac-seq", "atac seq", "dnase",
            "chromatin access", "nucleosome", "dna methylat", "cpg",
            "bisulfite", "bivalent", "super-enhancer", "topologically",
            "3d genome", "hi-c", "ctcf", "cohesin",
        ],
    ),
    "infectious_disease": (
        "Infectious Disease",
        [
            "infect", "virus", "viral", "bacteri", "pathogen", "host-pathogen",
            "sars-cov", "covid", "influenza", "hiv", "hepatitis",
            "tuberculosis", "malaria", "sepsis", "microbiom", "antimicrobial",
            "antibiotic", "antiviral", "vaccine", "parasit",
            "fungal", "mycobacteri", "staphylococc", "streptococc",
            "escherichia", "salmonella", "clostridi",
        ],
    ),
    "fibrosis_wound": (
        "Fibrosis & Wound Healing",
        [
            "fibros", "fibrotic", "wound heal", "scar", "scarring",
            "tissue repair", "regenerat", "collagen", "extracellular matrix",
            "ecm", "myofibroblast", "keloid", "pulmonary fibrosis", "ipf",
            "liver fibrosis", "renal fibrosis", "cardiac fibrosis",
        ],
    ),
    "aging": (
        "Aging & Senescence",
        [
            "aging", "ageing", "senescen", "longevity", "lifespan",
            "age-related", "geriatr", "old age", "young vs old",
            "rejuvenat", "telomer", "progeria", "gerontol",
        ],
    ),
    "kidney": (
        "Kidney & Renal",
        [
            "kidney", "renal", "nephro", "glomerul", "podocyte", "tubular",
            "proximal tubule", "distal tubule", "collecting duct",
            "chronic kidney", "acute kidney", "ckd", "aki", "dialysis",
        ],
    ),
    "gut_intestine": (
        "Gut & Intestinal Biology",
        [
            "intestin", "gut", "colon", "colonic", "colitis", "ibd",
            "crohn", "ileum", "ileal", "jejun", "duoden", "cecum",
            "cecal", "enterocyte", "goblet cell", "paneth", "crypt",
            "villus", "villi", "microbiota", "enteric",
        ],
    ),
    "lung_respiratory": (
        "Lung & Respiratory",
        [
            "lung", "pulmonary", "airway", "alveol", "bronch",
            "pneumo", "asthma", "copd", "respiratory", "trachea",
            "epithelial barrier", "surfactant", "cystic fibrosis",
        ],
    ),
    "skeletal_muscle": (
        "Muscle & Musculoskeletal",
        [
            "muscle", "skeletal muscle", "myocyte", "myoblast", "myofiber",
            "sarco", "dystrophy", "muscular", "bone", "osteo",
            "chondrocyte", "cartilage", "joint", "arthritis", "tendon",
        ],
    ),
    "skin": (
        "Skin & Dermatology",
        [
            "skin", "epiderm", "dermis", "keratinocyte", "melanocyte",
            "hair follicle", "wound", "psoriasis", "dermatit", "atopic",
            "cutaneous", "sebaceous",
        ],
    ),
    "reproduction": (
        "Reproductive Biology",
        [
            "reproduct", "fertility", "infertil", "ovary", "ovarian",
            "uterus", "uterin", "endometri", "placenta", "trophoblast",
            "testis", "testicular", "sperm", "oocyte", "follicle",
            "pregnancy", "pregnan", "implantation", "menstrual",
        ],
    ),
    "hematopoiesis": (
        "Hematopoiesis & Blood",
        [
            "hematopoie", "haematopoie", "bone marrow", "hsc", "hspc",
            "erythro", "megakaryocyte", "platelet", "myeloid",
            "granulocyte", "hematolog", "haematolog", "blood cell",
            "cord blood", "transplant", "graft", "engraftment",
            "clonal hematopoiesis",
        ],
    ),
    "crispr_gene_editing": (
        "CRISPR & Gene Editing",
        [
            "crispr", "cas9", "cas13", "gene edit", "genome edit",
            "guide rna", "grna", "sgrna", "knock-out", "knockout",
            "knock-in", "knockin", "perturb-seq", "perturbseq",
            "crop-seq", "cropseq",
        ],
    ),
    "drug_response": (
        "Drug Response & Pharmacology",
        [
            "drug respon", "drug resist", "pharmacol", "therapeut",
            "treatment respon", "chemotherapy", "targeted therapy",
            "inhibitor", "agonist", "antagonist", "dose-respon",
            "pharmacogenom", "drug sensitivity", "ic50",
        ],
    ),
    "plant_biology": (
        "Plant Biology",
        [
            "arabidopsis", "plant", "root", "leaf", "shoot",
            "photosynthes", "chloroplast", "phytohormone", "auxin",
            "cytokinin", "abscisic acid", "ethylene", "jasmonic",
            "salicylic acid", "pollen", "stamen", "pistil", "seed",
            "germination", "rice", "maize", "wheat", "tobacco",
            "tomato", "soybean", "oryza", "zea mays", "nicotiana",
        ],
    ),
}


def tag_topics(record):
    """Return list of matching topic keys for a record."""
    text = f"{record['title']} {record['summary']}".lower()
    tags = []
    for key, (name, keywords) in TOPICS.items():
        if any(kw in text for kw in keywords):
            tags.append(key)
    return tags


if __name__ == "__main__":
    with open("rnaseq_classified.json") as f:
        data = json.load(f)

    for r in data:
        r["topics"] = tag_topics(r)

    # Stats
    print("Topic distribution (multi-label, records can appear in multiple topics):\n")
    topic_counts = Counter()
    for r in data:
        for t in r["topics"]:
            topic_counts[t] += 1

    for key, count in topic_counts.most_common():
        name = TOPICS[key][0]
        print(f"  {count:>5}  {name}")

    untagged = [r for r in data if not r["topics"]]
    print(f"\n  Untagged: {len(untagged)}")
    print(f"  Total records: {len(data)}")

    print(f"\nSample untagged records:")
    for r in untagged[:15]:
        print(f"  {r['accession']}  {r['title'][:90]}")

    with open("rnaseq_classified.json", "w") as f:
        json.dump(data, f, indent=2)
    print("\nSaved updated classifications to rnaseq_classified.json")
