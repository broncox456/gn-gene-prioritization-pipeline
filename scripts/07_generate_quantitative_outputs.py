from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "results" / "prioritized_genes.tsv"

TABLES_DIR = BASE_DIR / "results" / "tables"
REPORTS_DIR = BASE_DIR / "results" / "reports"

TABLES_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE, sep="\t")

required_cols = {"gene", "log2FC", "padj", "renal_relevance", "classification", "priority_score"}
missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

total_genes = len(df)
significant_genes = df[df["padj"] < 0.05].shape[0]
upregulated = df[df["classification"] == "upregulated_significant"].shape[0]
downregulated = df[df["classification"] == "downregulated_significant"].shape[0]
not_significant = df[df["classification"] == "not_significant"].shape[0]
high_renal = df[df["renal_relevance"] == "high"].shape[0]
medium_renal = df[df["renal_relevance"] == "medium"].shape[0]
low_renal = df[df["renal_relevance"] == "low"].shape[0]

top_n = min(20, total_genes)
top_genes = df.head(top_n).copy()

summary = pd.DataFrame({
    "metric": [
        "Total genes analyzed",
        "Significant genes (padj < 0.05)",
        "Upregulated significant genes",
        "Downregulated significant genes",
        "Non-significant genes",
        "Genes with high renal relevance",
        "Genes with medium renal relevance",
        "Genes with low renal relevance",
        "Top genes exported"
    ],
    "value": [
        total_genes,
        significant_genes,
        upregulated,
        downregulated,
        not_significant,
        high_renal,
        medium_renal,
        low_renal,
        top_n
    ]
})

summary.to_csv(TABLES_DIR / "quantitative_summary.tsv", sep="\t", index=False)
top_genes.to_csv(TABLES_DIR / "top_20_prioritized_genes.tsv", sep="\t", index=False)

example_cols = ["gene", "log2FC", "padj", "renal_relevance", "classification", "priority_score"]
df[example_cols].head(10).to_csv(TABLES_DIR / "example_tsv_output.tsv", sep="\t", index=False)

report_text = f"""# Quantitative summary of the gene prioritization pipeline

The pipeline analyzed {total_genes} genes. Among them, {significant_genes} genes met the statistical significance criterion of adjusted p-value < 0.05.

Classification results:
- Upregulated significant genes: {upregulated}
- Downregulated significant genes: {downregulated}
- Non-significant genes: {not_significant}

Renal relevance distribution:
- High renal relevance: {high_renal}
- Medium renal relevance: {medium_renal}
- Low renal relevance: {low_renal}

The final prioritized table was ranked by priority score, integrating absolute log2 fold change, adjusted p-value, and renal relevance weight.

A top-{top_n} table was exported to:
results/tables/top_20_prioritized_genes.tsv

Note:
If the input dataset contains fewer than 20 genes, the script exports all available genes while preserving the top-20 naming convention for consistency with the final report.
"""

(REPORTS_DIR / "quantitative_results_summary.md").write_text(report_text, encoding="utf-8")

print("OK: quantitative summary generated")
print(summary)
