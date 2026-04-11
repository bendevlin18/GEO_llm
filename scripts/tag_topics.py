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
    "microbiology": (
        "Microbiology",
        [
            "bacteria", "bacterial", "biofilm", "quorum sensing",
            "virulence", "coloniz", "regulon", "operon", "sigma factor",
            "two-component", "ferment", "sporulat", "competence",
            "conjugat", "plasmid", "phage", "bacteriophage",
            "antimicrobial resist", "amr", "efflux pump",
            "gram-positive", "gram-negative", "proteobacteri",
            "actinobacteri", "firmicutes", "cyanobacteri",
            "yeast", "saccharomyces", "candida", "aspergillus",
            "fusarium", "penicillium", "trichoderma", "neurospora",
            "schizosaccharomyces", "cryptococcus", "pichia",
            "komagataella",
        ],
    ),
    "cell_stress": (
        "Cell Stress & Homeostasis",
        [
            "stress response", "heat shock", "cold shock", "osmotic",
            "oxidative stress", "reactive oxygen", "ros", "redox",
            "unfolded protein", "upr", "er stress", "endoplasmic reticulum stress",
            "autophagy", "autophag", "apoptosis", "apoptot",
            "programmed cell death", "necroptosis", "ferroptosis",
            "pyroptosis", "proteostasis", "proteasom", "ubiquitin",
            "hypoxia", "hypoxic", "hif-1", "ischemia", "ischemic",
            "nutrient deprivation", "starvation", "amino acid starvation",
            "dna damage", "dna repair", "genotoxic", "radiation",
            "irradiat", "uv response",
        ],
    ),
    "rna_biology": (
        "RNA Biology & Regulation",
        [
            "non-coding rna", "ncrna", "lncrna", "long non-coding",
            "mirna", "microrna", "micro-rna", "circrna", "circular rna",
            "pirna", "small rna", "srna", "snorna", "riboswitch",
            "rna binding", "rna-binding", "rbp", "rna processing",
            "alternative splicing", "splicing", "splice", "spliceosom",
            "rna stability", "mrna decay", "mrna degradat", "nonsense-mediated",
            "nmd", "rna editing", "a-to-i editing", "rna modific",
            "m6a", "rna methylat", "epitranscriptom",
            "polyadenylat", "poly(a)", "rna locali", "rna transport",
            "ribosome", "ribosom", "translat", "trna",
        ],
    ),
    "gene_regulation": (
        "Gene Regulation & Transcription",
        [
            "transcription factor", "transcriptional regulat",
            "gene regulat", "gene expression regulat",
            "regulatory network", "grn", "cis-regulat",
            "trans-regulat", "coactivator", "corepressor",
            "mediator complex", "rna polymerase", "pol ii",
            "transcription initiat", "transcription elongat",
            "transcription terminat", "promoter", "enhancer",
            "insulator", "boundary element",
        ],
    ),
    "cell_cycle": (
        "Cell Cycle & Proliferation",
        [
            "cell cycle", "mitosis", "mitotic", "meiosis", "meiotic",
            "cell division", "cell proliferat", "checkpoint",
            "cyclin", "cdk", "s phase", "g1 phase", "g2 phase",
            "m phase", "dna replicat", "centromere", "kinetochore",
            "spindle", "cytokinesis", "aneuploidy", "polyploid",
        ],
    ),
    "signal_transduction": (
        "Signal Transduction",
        [
            "signal", "signaling", "signalling", "pathway",
            "wnt", "notch", "hedgehog", "tgf-beta", "tgfb",
            "bmp", "mapk", "erk", "jnk", "p38",
            "pi3k", "akt", "mtor", "nf-kb", "nfkb",
            "jak-stat", "stat3", "stat5", "receptor tyrosine",
            "phosphorylat", "kinase", "phosphatase",
            "g protein", "gpcr", "camp", "calcium signal",
        ],
    ),
    "eye_vision": (
        "Eye & Vision",
        [
            "retina", "retinal", "cornea", "corneal", "lens",
            "optic nerve", "photoreceptor", "rod cell", "cone cell",
            "macula", "macular degenerat", "glaucoma", "ocular",
            "intraocular", "vitreous", "choroid", "rpe",
            "retinal pigment", "visual", "blindness",
        ],
    ),
    "liver": (
        "Liver & Hepatology",
        [
            "liver", "hepatic", "hepatocyte", "hepato",
            "cirrhosis", "steatosis", "nafld", "nash", "mafld",
            "masld", "mash", "biliary", "bile", "cholestasis",
            "portal", "sinusoid", "kupffer", "stellate cell",
            "liver fibrosis", "liver cancer", "hcc",
            "hepatoblastoma", "liver regenerat", "liver injury",
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
