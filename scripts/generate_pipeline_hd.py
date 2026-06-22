import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(16,4))

ax.set_xlim(0, 100)
ax.set_ylim(0, 20)

ax.axis("off")

steps = [
    ("INPUT DATA", 2),
    ("PYTHON\nPROCESSING", 22),
    ("PRIORITY\nSCORE", 42),
    ("GENE\nRANKING", 62),
    ("OUTPUTS", 82)
]

for label, x in steps:

    box = FancyBboxPatch(
        (x, 6),
        14,
        8,
        boxstyle="round,pad=0.4",
        linewidth=2
    )

    ax.add_patch(box)

    ax.text(
        x + 7,
        10,
        label,
        ha="center",
        va="center",
        fontsize=12,
        weight="bold"
    )

# Flechas
for x in [16,36,56,76]:

    ax.annotate(
        "",
        xy=(x+4,10),
        xytext=(x,10),
        arrowprops=dict(
            arrowstyle="->",
            lw=2
        )
    )

plt.title(
    "Reproducible Bioinformatics Pipeline",
    fontsize=18,
    weight="bold"
)

plt.tight_layout()

plt.savefig(
    "results/figures_hd/pipeline_hd.png",
    dpi=300,
    bbox_inches="tight"
)

print("OK: Pipeline HD exportado")
