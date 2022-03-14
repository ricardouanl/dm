import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("csv/mineria_datos_f1_positions.csv")

min = df.min(axis=1,numeric_only=True)
max = df.max(axis=1,numeric_only=True)
mean = df.mean(axis=1,numeric_only=True).round(2)
mode = df.mode(axis=1,numeric_only=True)[0]
count = df.count(axis=1,numeric_only=True)
sum = df.sum(axis=1,numeric_only=True)
kurtosis = df.kurtosis(axis=1,numeric_only=True).round(2)
var = df.var(axis=1,numeric_only=True).round(2)
std = df.std(axis=1,numeric_only=True).round(2)

df['min'] = min
df['max'] = max
df['mean'] = mean
df['mode'] = mode
df['count'] = count
df['sum'] = sum
df['kurtosis'] = kurtosis
df['var'] = var
df['std'] = std

print_tabulate(df)
df.to_csv("csv/mineria_datos_f1_positions_with_stats.csv", index=False)
