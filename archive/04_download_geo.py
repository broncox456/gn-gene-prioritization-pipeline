from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_FILE = BASE_DIR / "data" / "external" / "geo_mock_dataset.tsv"

def main():
    print("Simulando dataset tipo GEO...")

    data = {
        "gene": ["NPHS1", "WT1", "IL6", "TNF", "UMOD", "COL4A4", "CXCL8"],
        "log2FC": [2.5, 1.7, 3.2, 2.8, -1.8, -2.6, 2.9],
        "padj": [0.001, 0.02, 0.0004, 0.003, 0.03, 0.002, 0.004],
        "renal_relevance": ["high", "high", "medium", "medium", "high", "high", "medium"]
    }

    df = pd.DataFrame(data)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, sep="\t", index=False)

    print("OK: dataset generado correctamente")

if __name__ == "__main__":
    main()