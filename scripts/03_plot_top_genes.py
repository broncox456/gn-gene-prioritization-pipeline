from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "results" / "prioritized_genes.tsv"
OUTPUT_FILE = BASE_DIR / "results" / "figures" / "top_genes.png"

def main():
    print("Cargando resultados priorizados...")
    df = pd.read_csv(INPUT_FILE, sep="\t")

    if df.empty:
        raise ValueError("El archivo está vacío.")

    top_df = df.head(5)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.bar(top_df["gene"], top_df["priority_score"])
    plt.title("Top 5 genes priorizados")
    plt.xlabel("Gen")
    plt.ylabel("Priority score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=300)

    print("OK: figura generada correctamente")

if __name__ == "__main__":
    main()