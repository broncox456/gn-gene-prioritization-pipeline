# Semana 4

## Objetivo
Adaptar el pipeline para trabajar con un dataset externo con estructura similar a un conjunto de datos procedente de GEO.

## Actividades realizadas
- Se creó un script adicional para generar un dataset externo estructurado.
- Se almacenó el nuevo archivo en la carpeta `data/external`.
- Se modificó el pipeline principal para que leyera el dataset externo en lugar del dataset de prueba inicial.
- Se ejecutó nuevamente el flujo de análisis completo, incluyendo priorización, validación y visualización.

## Resultados
El pipeline pudo procesar correctamente un dataset externo manteniendo la misma lógica de análisis, validación estructural y generación de figura.

## Observaciones
Esta etapa permitió separar con mayor claridad los datos de prueba de los datos externos y preparar la transición hacia el uso de datasets públicos reales.

## Dificultades encontradas
- Fue necesario verificar cuidadosamente la ruta de entrada del script principal.
- También fue importante mantener el mismo formato de columnas para no romper el flujo de trabajo ya construido.

## Próximo paso
Descargar y procesar un dataset real de GEO para sustituir progresivamente el dataset externo simulado.