# Semana 2

## Objetivo
Mejorar la estabilidad del pipeline y validar correctamente los resultados generados.

## Actividades realizadas
- Se corrigió el problema inicial de ejecución en Windows, unificando el uso del intérprete Python mediante el comando `py`.
- Se instaló la librería pandas para el manejo de datos tabulares.
- Se revisó la salida generada en la semana 1 y se identificó que la puntuación tenía demasiados decimales.
- Se implementó redondeo del `priority_score` para mejorar la consistencia de los resultados.
- Se ajustó el ordenamiento de los genes para garantizar estabilidad en la salida.
- Se desarrolló un script de validación estructural que verifica:
  - columnas esperadas
  - archivo no vacío
  - orden descendente correcto

## Resultados
El pipeline ahora genera una salida más estable, reproducible y consistente.  
La validación confirma que la estructura del resultado es correcta.

## Observaciones
Los genes mejor posicionados (IL6, NPHS1, COL4A4) tienen relevancia biológica en procesos inflamatorios y daño glomerular, lo cual es coherente con el enfoque clínico del proyecto.

## Dificultades encontradas
- Problemas iniciales con la ejecución de Python en Windows debido a múltiples intérpretes.
- Falta de instalación de dependencias (pandas).
- Diferencias en precisión numérica que afectaban la validación inicial.

## Próximo paso
Incorporar una visualización de los genes priorizados para mejorar la interpretación de los resultados.