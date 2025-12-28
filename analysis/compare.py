#!/usr/bin/env python3
"""
Compare sustainability of piping materials.
"""

import csv
import os

def calculate_score(row):
    """
    Calculate Sustainability Score based on weighted factors.
    """
    renewable = float(row['Renewable_Content_Percent'])
    lifespan = float(row['Average_Lifespan_years'])
    recyclability = float(row['Recyclability_Percent'])
    energy = float(row['Estimated_Production_Energy_MJ_per_kg'])
    carbon = float(row['Estimated_Carbon_Footprint_kg_CO2e_per_kg'])
    
    # Weights as defined in methodology
    score = (renewable * 0.3) + (lifespan * 0.25) + (recyclability * 0.2) - (energy * 0.15) - (carbon * 0.1)
    return round(score, 2)

def main():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'material_data.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            materials = []
            for row in reader:
                score = calculate_score(row)
                materials.append({
                    'name': row['Material_Name'],
                    'score': score,
                    'raw_material': row['Primary_Raw_Material'],
                    'renewable': row['Renewable_Content_Percent'],
                    'lifespan': row['Average_Lifespan_years'],
                    'recyclability': row['Recyclability_Percent'],
                    'energy': row['Estimated_Production_Energy_MJ_per_kg'],
                    'carbon': row['Estimated_Carbon_Footprint_kg_CO2e_per_kg']
                })
    except FileNotFoundError:
        print(f"Error: Could not find data file at {csv_path}")
        return
    
    # Sort by score descending
    materials.sort(key=lambda x: x['score'], reverse=True)
    
    # Print results
    print("Sustainable Piping Analysis - Ranked Materials")
    print("=" * 60)
    for i, mat in enumerate(materials, 1):
        print(f"{i}. {mat['name']} (Score: {mat['score']})")
        print(f"   Raw Material: {mat['raw_material']}")
        print(f"   Renewable: {mat['renewable']}%, Lifespan: {mat['lifespan']} years, Recyclability: {mat['recyclability']}%")
        print(f"   Production Energy: {mat['energy']} MJ/kg, Carbon Footprint: {mat['carbon']} kg CO2e/kg")
        print()

if __name__ == "__main__":
    main()