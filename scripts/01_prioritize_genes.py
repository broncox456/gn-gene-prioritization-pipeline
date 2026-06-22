from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "external" / "geo_real_dataset.tsv"
OUTPUT_FILE = BASE_DIR / "results" / "prioritized_genes.tsv"

RENAL_WEIGHTS = {
    "high": 3,
    "medium": 2,
    "low": 1
}

def classify_gene(log2fc, padj):
    if padj < 0.05 and log2fc > 1:
        return "upregulated_significant"
    elif padj < 0.05 and log2fc < -1:
        return "downregulated_significant"
    else:
        return "not_significant"

def main():
    print("Cargando datos...")
    df = pd.read_csv(INPUT_FILE, sep="\t")

    required_cols = {"gene", "log2FC", "padj", "renal_relevance"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")

    print("Procesando genes...")
    df["classification"] = df.apply(
        lambda row: classify_gene(row["log2FC"], row["padj"]),
        axis=1
    )

    df["renal_weight"] = df["renal_relevance"].map(RENAL_WEIGHTS).fillna(1)

    df["priority_score"] = (
        df["log2FC"].abs() * df["renal_weight"]
    ) / (df["padj"] + 1e-6)

    df["priority_score"] = df["priority_score"].round(4)

    df = df.sort_values(
        by=["priority_score", "gene"],
        ascending=[False, True]
    ).reset_index(drop=True)

    print("Guardando resultados...")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, sep="\t", index=False)

    print("OK: pipeline ejecutado correctamente")

if __name__ == "__main__":
    main()