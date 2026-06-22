from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RESULTS_FILE = BASE_DIR / "results" / "prioritized_genes.tsv"
TABLES_DIR = BASE_DIR / "results" / "tables"
REPORTS_DIR = BASE_DIR / "results" / "reports"

TABLES_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RESULTS_FILE, sep="\t")

clinical_notes = {
    "IL6": [
        "Inflammatory activation and cytokine signaling",
        "IL6 is associated with inflammatory activity that may contribute to glomerular injury.",
        "Supports inflammatory component of glomerulonephritis."
    ],
    "TNF": [
        "Pro-inflammatory signaling",
        "TNF participates in inflammatory amplification and renal damage.",
        "Reinforces inflammation in disease progression."
    ],
    "COL4A4": [
        "Basement membrane structure",
        "Key structural protein in glomerular basement membrane.",
        "Suggests structural involvement in disease."
    ],
    "NPHS1": [
        "Podocyte integrity",
        "Encodes nephrin, essential for filtration barrier.",
        "Supports podocyte injury relevance."
    ]
}

rows = []

for _, row in df.iterrows():
    gene = str(row["gene"])
    note = clinical_notes.get(gene, [
        "Not curated",
        "Requires literature review",
        "Exploratory interpretation"
    ])

    rows.append({
        "gene": gene,
        "log2FC": row["log2FC"],
        "padj": row["padj"],
        "priority_score": row["priority_score"],
        "classification": row["classification"],
        "biological_process": note[0],
        "renal_interpretation": note[1],
        "clinical_relevance": note[2]
    })

clinical_df = pd.DataFrame(rows)

clinical_df.to_csv(TABLES_DIR / "clinical_gene_interpretation.tsv", sep="\t", index=False)

report = "Clinical interpretation of prioritized genes\n\n"

for _, row in clinical_df.head(10).iterrows():
    report += f"{row['gene']}: {row['renal_interpretation']} ({row['clinical_relevance']})\n"

(REPORTS_DIR / "clinical_interpretation_summary.md").write_text(report)

print("OK: clinical interpretation generated")