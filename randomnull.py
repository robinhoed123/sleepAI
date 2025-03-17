import pandas as pd
import numpy as np
import random

def set_random_nulls(csv_file, columns, num_nulls, seed=None, output_file=None):
    # Stel de seed in voor de random generator
    if seed is not None:
        random.seed(seed)
    
    # Lees het CSV-bestand in een DataFrame
    df = pd.read_csv(csv_file)
    
    for col, null_count in zip(columns, num_nulls):
        if col < len(df.columns):
            # Selecteer willekeurige indices om null te zetten
            indices = random.sample(range(len(df)), null_count)
            df.iloc[indices, col] = np.nan
    
    # Sla het gewijzigde DataFrame op naar een nieuw CSV-bestand als output_file is opgegeven
    if output_file is not None:
        df.to_csv(output_file, index=False)
    
    return df

# Voorbeeld gebruik
csv_file = 'sleep_cycle_productivity.csv'
columns = [2, 3,6,7,8,9,10,11]  # Kolommen om nulls in te zetten
num_nulls = [20, 30,5,14,27,17,8,12]  # Aantal null-waarden per kolom
seed = 42 
output_file = 'sleep_cycle_productivity2.csv'  # Pad nieuw bestand

df_with_nulls = set_random_nulls(csv_file, columns, num_nulls, seed, output_file)
print(df_with_nulls)