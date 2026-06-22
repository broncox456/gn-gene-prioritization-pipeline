from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RESULT_FILE = BASE_DIR / "results" / "prioritized_genes.tsv"

EXPECTED_COLUMNS = [
    "gene",
    "log2FC",
    "padj",
    "renal_relevance",
    "classification",
    "renal_weight",
    "priority_score"
]

def main():
    print("Validando salida del pipeline...")
    df = pd.read_csv(RESULT_FILE, sep="\t")

    missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Faltan columnas esperadas: {missing_cols}")

    if df.empty:
        raise ValueError("El archivo de resultados está vacío.")

    if not df["priority_score"].is_monotonic_decreasing:
        raise ValueError("Los genes no están ordenados de mayor a menor priority_score.")

    print("OK: validación estructural correcta")
    print(f"Número de genes: {len(df)}")
    print("Top 5 genes:")
    print(df[["gene", "priority_score"]].head())

if __name__ == "__main__":
    main()