# Pipeline Bioinformático para Priorización de Genes en Glomerulonefritis

**Autor:** Cristian Arias Ramírez
**Máster:** Máster Universitario en Bioinformática – Universidad Alfonso X el Sabio (UAX)
**Proyecto:** Memoria de Prácticas Académicas Externas
**Año:** 2026

---

# Descripción general

Este repositorio contiene un pipeline bioinformático reproducible desarrollado en Python para la priorización de genes candidatos en glomerulonefritis.

El proyecto tiene carácter académico y formativo y fue desarrollado en un entorno *in silico* utilizando datasets estructurados de expresión génica. Su finalidad es demostrar la construcción de un flujo de trabajo reproducible capaz de:

* Procesar datos tabulares.
* Priorizar genes candidatos.
* Generar resultados estructurados.
* Crear visualizaciones interpretables.
* Implementar mecanismos de trazabilidad y reproducibilidad.

Los datasets empleados están inspirados en estructuras utilizadas habitualmente en repositorios transcriptómicos públicos; sin embargo, no corresponden a matrices transcriptómicas crudas descargadas directamente de GEO (Gene Expression Omnibus).

---

# Repositorio del proyecto

**GitHub:**

https://github.com/broncox456/gn-gene-prioritization-pipeline

Este repositorio acompaña la Memoria de Prácticas Académicas Externas del Máster Universitario en Bioinformática de la Universidad Alfonso X el Sabio (UAX).

---

# Objetivo del proyecto

Desarrollar un pipeline reproducible para priorizar genes candidatos relacionados con glomerulonefritis mediante la integración de:

* Magnitud del cambio de expresión génica.
* Significación estadística.
* Relevancia renal asignada.
* Generación de rankings reproducibles.
* Visualización de resultados.
* Registro de ejecuciones y trazabilidad.

---

# Alcance

Este proyecto no constituye una herramienta diagnóstica, predictiva ni de validación clínica de biomarcadores.

Los resultados deben interpretarse exclusivamente como una demostración metodológica y formativa del funcionamiento de un pipeline bioinformático orientado a la priorización génica.

---

# Estructura del proyecto

```text
gn_gene_prioritization/
│
├── data/
│   ├── raw/
│   ├── external/
│   └── processed/
│
├── scripts/
│   ├── 01_prioritize_genes.py
│   ├── 02_validate_output.py
│   ├── 03_plot_top_genes.py
│   ├── 07_generate_quantitative_outputs.py
│   ├── 08_generate_required_figures.py
│   ├── 09_generate_clinical_interpretation.py
│   └── r_analysis/
│
├── results/
│   ├── figures/
│   ├── figures_hd/
│   ├── reports/
│   ├── tables/
│   └── prioritized_genes.tsv
│
├── logs/
├── archive/
├── requirements.txt
├── run_pipeline.ps1
└── README.md
```

---

# Herramientas utilizadas

| Herramienta | Función                     |
| ----------- | --------------------------- |
| Python      | Desarrollo del pipeline     |
| pandas      | Manipulación de datos       |
| matplotlib  | Visualización               |
| PowerShell  | Automatización              |
| Git         | Control de versiones        |
| R           | Actividades exploratorias   |
| limma       | Expresión diferencial       |
| DESeq2      | Revisión conceptual RNA-seq |

---

# Instalación

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

# Ejecución del pipeline

```powershell
powershell -ExecutionPolicy Bypass -File .\run_pipeline.ps1
```

Los resultados se almacenarán automáticamente en:

```text
results/
logs/
```

---

# Salidas principales

| Archivo                                            | Descripción                          |
| -------------------------------------------------- | ------------------------------------ |
| results/prioritized_genes.tsv                      | Tabla principal de genes priorizados |
| results/tables/top_20_prioritized_genes.tsv        | Ranking de genes                     |
| results/tables/quantitative_summary.tsv            | Resumen cuantitativo                 |
| results/tables/clinical_gene_interpretation.tsv    | Interpretación conceptual            |
| results/figures/figure_1_top_prioritized_genes.png | Figura principal                     |
| results/figures/figure_2_pipeline_diagram.png      | Diagrama del pipeline                |
| results/figures/figure_3_example_tsv_output.png    | Ejemplo de salida TSV                |
| logs/runlog_*.txt                                  | Registros de ejecución               |

---

# Reproducibilidad

El proyecto incorpora mecanismos básicos de reproducibilidad:

* Organización modular de carpetas.
* Separación de scripts por funcionalidad.
* Archivo `requirements.txt`.
* Automatización mediante PowerShell.
* Registro de ejecuciones en `logs`.
* Validación mediante *expected outputs*.
* Control de versiones con Git.
* Documentación técnica mediante este README.

---

# Interpretación de resultados

El sistema genera un ranking de genes priorizados a partir de:

* Magnitud del cambio de expresión génica.
* Valor p ajustado.
* Relevancia renal asignada.

La interpretación biológica de los resultados se realiza exclusivamente con fines educativos y de validación conceptual del pipeline.

Los resultados no deben considerarse evidencia clínica directa, validación funcional de biomarcadores ni recomendaciones diagnósticas o terapéuticas.

---

# Relación con la Memoria de Prácticas

El contenido técnico de este repositorio se encuentra alineado con la Memoria de Prácticas Académicas Externas presentada en el Máster Universitario en Bioinformática de la Universidad Alfonso X el Sabio (UAX), donde se describen:

* El desarrollo progresivo del pipeline.
* Los mecanismos de reproducibilidad.
* Las limitaciones metodológicas.
* La aplicación conceptual a la priorización génica en glomerulonefritis.

---

# Limitaciones

* Dataset reducido y estructurado con fines formativos.
* No se utilizan matrices transcriptómicas crudas descargadas directamente de GEO.
* No existe validación experimental independiente.
* No se implementan modelos predictivos ni aprendizaje automático.
* No se realiza corrección de efectos de batch.
* No se contempla integración multi-ómica.
* Las actividades realizadas en R tienen carácter exploratorio y formativo.

---

# Uso académico

Este proyecto fue desarrollado exclusivamente con fines académicos dentro del Máster Universitario en Bioinformática de la Universidad Alfonso X el Sabio (UAX).

Su contenido está destinado a la demostración de competencias en programación, análisis de datos, reproducibilidad y bioinformática aplicada a enfermedades renales.

---

# Cómo citar este repositorio

Arias Ramírez C. Pipeline Bioinformático para Priorización de Genes en Glomerulonefritis. Máster Universitario en Bioinformática, Universidad Alfonso X el Sabio (UAX), 2026.

---

# Licencia

Uso exclusivamente académico y educativo.
Todos los derechos reservados © Cristian Arias Ramírez, 2026.
