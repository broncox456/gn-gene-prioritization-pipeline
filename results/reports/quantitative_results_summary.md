# Quantitative summary of the gene prioritization pipeline

The pipeline analyzed 10 genes. Among them, 10 genes met the statistical significance criterion of adjusted p-value < 0.05.

Classification results:
- Upregulated significant genes: 8
- Downregulated significant genes: 2
- Non-significant genes: 0

Renal relevance distribution:
- High renal relevance: 5
- Medium renal relevance: 5
- Low renal relevance: 0

The final prioritized table was ranked by priority score, integrating absolute log2 fold change, adjusted p-value, and renal relevance weight.

A top-10 table was exported to:
results/tables/top_20_prioritized_genes.tsv

Note:
If the input dataset contains fewer than 20 genes, the script exports all available genes while preserving the top-20 naming convention for consistency with the final report.
