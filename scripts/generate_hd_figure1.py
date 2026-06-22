import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv(
    "data/external/geo_real_dataset.tsv",
    sep="\t"
)

# Crear priority score
df["priority_score"] = (
    abs(df["log2FC"]) *
    (-df["padj"].apply(lambda x: math.log10(x)))
)

# Top genes
top = df.sort_values(
    "priority_score",
    ascending=False
).head(10)

# Figura profesional HD
plt.figure(figsize=(10,6))

plt.barh(
    top["gene"],
    top["priority_score"]
)

plt.xlabel(
    "Priority Score",
    fontsize=12
)

plt.ylabel(
    "Genes",
    fontsize=12
)

plt.title(
    "Top Prioritized Genes",
    fontsize=16,
    weight="bold"
)

plt.gca().invert_yaxis()

plt.tight_layout()

# Exportar HD
plt.savefig(
    "results/figures_hd/top_prioritized_genes_hd.png",
    dpi=300,
    bbox_inches="tight"
)

print("OK: Figura 1 HD exportada")
