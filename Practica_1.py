import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

# Custom
def get_data_frame_lcc() -> pd.DataFrame:
    soup = get_soup("http://www.fcfm.uanl.mx/es/licenciatura/plandeestudios/LCC2017")
    list_of_lists = []
    rows = soup.find_all('tr')
    for row in rows[1:]:
        columns = row.find_all('td')
        listado_de_valores_en_columnas = [column.text.strip() for column in columns]
        list_of_lists.append(listado_de_valores_en_columnas)
    return pd.DataFrame(list_of_lists, columns=[header.text.strip() for header in rows[0].find_all('th')])


df = get_data_frame_lcc()
print_tabulate(df)
df.to_csv("csv/materias_lcc.csv", index=False)
# ======
