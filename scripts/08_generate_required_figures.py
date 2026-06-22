from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BASE_DIR = Path(__file__).resolve().parents[1]
RESULTS_FILE = BASE_DIR / "results" / "prioritized_genes.tsv"
TABLE_FILE = BASE_DIR / "results" / "tables" / "example_tsv_output.tsv"
FIGURES_DIR = BASE_DIR / "results" / "figures"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RESULTS_FILE, sep="\t")

# Figure 1: Top prioritized genes
top_n = min(20, len(df))
top_df = df.head(top_n).sort_values("priority_score", ascending=True)

plt.figure(figsize=(10, 7))
plt.barh(top_df["gene"], top_df["priority_score"])
plt.xlabel("Priority score")
plt.ylabel("Gene")
plt.title(f"Top {top_n} prioritized genes in glomerulonephritis")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "figure_1_top_prioritized_genes.png", dpi=300)
plt.close()

# Figure 2: Pipeline diagram
steps = [
    "Input expression table",
    "Column validation",
    "Gene classification",
    "Priority score calculation",
    "Ranked TSV output",
    "Tables, figures and clinical interpretation"
]

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis("off")

x_positions = [0.02, 0.19, 0.36, 0.53, 0.70, 0.87]
for i, (x, step) in enumerate(zip(x_positions, steps)):
    box = FancyBboxPatch(
        (x, 0.42), 0.12, 0.22,
        boxstyle="round,pad=0.02",
        linewidth=1.5,
        facecolor="white",
        edgecolor="black"
    )
    ax.add_patch(box)
    ax.text(x + 0.06, 0.53, step, ha="center", va="center", fontsize=8, wrap=True)

    if i < len(steps) - 1:
        ax.annotate(
            "",
            xy=(x_positions[i + 1] - 0.01, 0.53),
            xytext=(x + 0.14, 0.53),
            arrowprops=dict(arrowstyle="->", linewidth=1.5)
        )

ax.set_title("Reproducible gene prioritization pipeline", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "figure_2_pipeline_diagram.png", dpi=300)
plt.close()

# Figure 3: TSV example as table image
example_df = pd.read_csv(TABLE_FILE, sep="\t").head(8)

fig, ax = plt.subplots(figsize=(13, 4))
ax.axis("off")
table = ax.table(
    cellText=example_df.values,
    colLabels=example_df.columns,
    cellLoc="center",
    loc="center"
)
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.4)
ax.set_title("Example of standardized TSV output", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "figure_3_example_tsv_output.png", dpi=300)
plt.close()

print("OK: required figures generated")
print(FIGURES_DIR)
