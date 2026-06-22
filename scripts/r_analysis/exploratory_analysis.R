# ============================================================
# exploratory_analysis.R
# Analisis exploratorio de expresion diferencial
# Herramientas: limma, DESeq2 (modo exploratorio)
# Autor: Cristian Arias Ramirez
# ============================================================

# Este script tiene un objetivo exploratorio y documental.
# No reemplaza un pipeline completo de expresion diferencial.
# DESeq2 requiere matriz de conteos crudos.
# limma requiere matriz de expresion normalizada.

if (!requireNamespace("limma", quietly = TRUE)) {
  message("limma no instalado. Instalar con: BiocManager::install('limma')")
} else {
  library(limma)
}

if (!requireNamespace("DESeq2", quietly = TRUE)) {
  message("DESeq2 no instalado. Instalar con: BiocManager::install('DESeq2')")
} else {
  library(DESeq2)
}

data_path <- file.path("data", "external", "geo_real_dataset.tsv")

if (!file.exists(data_path)) {
  stop("Archivo no encontrado: ", data_path)
}

df <- read.delim(data_path, sep = "\t", header = TRUE, stringsAsFactors = FALSE)

cat("Dataset cargado:", nrow(df), "genes\n")
cat("Columnas:", paste(colnames(df), collapse = ", "), "\n")

cat("\nResumen de log2FC:\n")
print(summary(df$log2FC))

cat("\nResumen de padj:\n")
print(summary(df$padj))

df$direction <- ifelse(
  df$log2FC > 1 & df$padj < 0.05,
  "upregulated",
  ifelse(
    df$log2FC < -1 & df$padj < 0.05,
    "downregulated",
    "not_significant"
  )
)

cat("\nDistribucion por clasificacion:\n")
print(table(df$direction))

cat("\nDistribucion por relevancia renal:\n")
print(table(df$renal_relevance))

if (!dir.exists("results/tables")) {
  dir.create("results/tables", recursive = TRUE)
}

output_path <- file.path("results", "tables", "r_exploratory_summary.tsv")
write.table(df, file = output_path, sep = "\t", row.names = FALSE, quote = FALSE)

cat("\nResultado exportado a:", output_path, "\n")

cat("\nNOTA METODOLOGICA:\n")
cat("Este script es exploratorio.\n")
cat("Un pipeline DESeq2 completo requiere matriz de conteos crudos.\n")
cat("Un pipeline limma completo requiere matriz de expresion normalizada.\n")
cat("Este analisis documenta la coherencia exploratoria con el scoring heuristico implementado en Python.\n")
