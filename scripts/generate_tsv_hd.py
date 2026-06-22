import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/external/geo_real_dataset.tsv",
    sep="\t"
)

preview = df.head(10)

fig, ax = plt.subplots(figsize=(12,4))

ax.axis("off")

table = ax.table(
    cellText=preview.values,
    colLabels=preview.columns,
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.5)

plt.title(
    "Example TSV Output",
    fontsize=16,
    weight="bold"
)

plt.savefig(
    "results/figures_hd/tsv_output_hd.png",
    dpi=300,
    bbox_inches="tight"
)

print("OK: TSV HD exportado")
