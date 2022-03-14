import io
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

# Custom
def get_area_from_nota(col_value:str):
    end = col_value.find('.') + 3
    return col_value[42:end]

def sanitize_booleans(col_value:str):
    yes_array = ['SI', 'si', 'Si']
    return col_value in yes_array

df = pd.read_csv("csv/parques_sn.csv")
df = df.rename(str.lower, axis='columns')

    # Remove Duplicates
df = df.drop_duplicates(subset=['numero_identificacion'])

    # Columns
df = df.rename(columns={"nota":"area"})
df = df.drop(["numero_identificacion",
    "ejercicio",
    "mes",
    "tipo_asentamiento",
    "tipo_vialidad",
    "cantidad_botes",
    ], axis=1)

    # Booleans
df['pista'] = df['pista'].transform(sanitize_booleans)
df['juegos_parque'] = df['juegos_parque'].transform(sanitize_booleans)
df['aparatos_ejercicio'] = df['aparatos_ejercicio'].transform(sanitize_booleans)
df['cancha'] = df['cancha'].transform(sanitize_booleans)
df['bebederos'] = df['bebederos'].transform(sanitize_booleans)
df['botes_basura'] = df['botes_basura'].transform(sanitize_booleans)

    # Data
df['area'] = df['area'].transform(get_area_from_nota)


print_tabulate(df)
df.to_csv("csv/parques_sn_limpios.csv", index=False)
# ======
