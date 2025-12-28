# Sustainable Piping Analysis

A tool for comparing the sustainability metrics of common piping materials, including PVC, copper, and HDPE.

## Methodology

The Sustainability Score is calculated as a weighted average of renewable content, lifespan, and recyclability, with penalties for energy use and carbon footprint.

Weights:
- Renewable_Content_Percent: 30%
- Average_Lifespan_years: 25%
- Recyclability_Percent: 20%
- Estimated_Production_Energy_MJ_per_kg: -15% (lower is better)
- Estimated_Carbon_Footprint_kg_CO2e_per_kg: -10% (lower is better)

Score = (Renewable_Content_Percent * 0.3) + (Average_Lifespan_years * 0.25) + (Recyclability_Percent * 0.2) - (Estimated_Production_Energy_MJ_per_kg * 0.15) - (Estimated_Carbon_Footprint_kg_CO2e_per_kg * 0.1)

## How to Run

1. Ensure Python 3 is installed.
2. Clone this repository.
3. Navigate to the repository directory.
4. Run the analysis script:
   ```bash
   python analysis/compare.py
   ```

## Data

The dataset includes sample data for PVC, Copper, PEX (cross-linked polyethylene), and Galvanized Steel. Each material is characterized by raw material source, renewable content percentage, production energy, carbon footprint, average lifespan, and recyclability percentage.

## Future Work

This tool can be extended to include performance metrics such as water pressure and temperature resistance factors.