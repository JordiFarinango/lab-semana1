# Lab semana 1 - Communities and Crime

- Persona A: Adrián Farinango
- Persona B: Cesar Toapanta
- Dataset: https://archive.ics.uci.edu/dataset/183/communities+and+crime
- Tarea: regresion Variable objetivo: ViolentCrimesPerPop
- Por que lo elegimos: Elegimos Communities and Crime porque es un problema de regresion con una gran cantidad de valores faltantes codificados como ?, lo que nos permite realizar la exploracion y limpieza de datos.

## Como correr

uv sync
uv run pytest -q
uv run python main.py

## Hallazgos
- (Persona A): Se detectaron 39,202 valores faltantes distribuidos en 25 columnas, 22 columnas presentan aproximadamente el 84% de nulos, mientras que county y community presentan cerca del 59% y OtherPerCap solo un valor faltante

## Decisiones de limpieza
- Se eliminaron las 22 columnas que tenían aproximadamente 84 % de valores nulos, ya que conservarlas implicaría trabajar con muy poca información disponible.
- Se eliminaron las columnas county y community, que tenían aproximadamente 59 % de valores nulos y corresponden a códigos de identificación, por lo que no era adecuado imputarlas con una medida como la mediana.
- OtherPerCap tenía un solo valor faltante (aproximadamente 0.05 %), por lo que se imputó con la mediana de la columna.
- Se verificaron valores infinitos y filas duplicadas; el dataset no presentó ninguno, pero la función de limpieza los contempla.
- La columna de texto communityname se normalizó eliminando espacios en los extremos y convirtiendo el texto a minúsculas.
