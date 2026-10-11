# Autonomous Drone Data Pipeline

## Overview
This repository contains an Object-Oriented Python data pipeline built with **Pandas**. It demonstrates the foundational data wrangling steps required before feeding raw, unstructured data into a Machine Learning algorithm or Neural Network. 

Machine learning models crash when encountering missing values, unaligned columns, or text categories. This pipeline ingests raw dictionaries representing an autonomous drone fleet and mathematically transforms them into a clean, model-ready feature matrix.

## Core Data Science Pillars Demonstrated
This project systematically applies the four core pillars of data preparation:

1. **Data Ingestion & Framing:** Converting unoptimized data structures (Python dictionaries) into high-performance, 2-dimensional C-engine matrices (`pd.DataFrame`).
2. **Slicing & Boolean Masking:** Surgically filtering the matrix using conditional logic to extract specific operational states (e.g., isolating drones with `< 50%` battery).
3. **Handling Corrupted Data:** Diagnosing and neutralizing `NaN` (Not a Number) values using `.fillna()` to prevent fatal algorithm crashes during model training.
4. **Relational Merging:** Performing in-memory SQL-style horizontal joins (`pd.merge()`) to stitch distinct datasets (fleet telemetrics and maintenance records) together using shared primary keys.
5. **Feature Engineering & Grouping:** Using vectorized math to create new predictive columns (`cost_per_hour`) and aggregating the data (`.groupby()`) to generate statistical summaries by drone model.

## Technology Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas

## Execution
Run the pipeline directly from the terminal to view the step-by-step mathematical transformations:
```bash
python drone_pipeline.py
