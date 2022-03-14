import pandas as pd

df = pd.read_csv("csv/mineria_datos_f1_positions_with_stats.csv")
df = df.fillna(19)

drivers_for_line_graph = 4
data = {}
for index in range(drivers_for_line_graph):
	row = list(df.iloc[index])
	data[row[0]] = row[1:23]


# Graphs

df_lines = pd.DataFrame(data, index=( list(range(1,23) ))) 
df_lines.plot.line(
	title='F1 TOP 4',
	xlabel='Races',
	ylabel='Position',
	figsize=(15,9),
	ylim=(0,20),
	xticks=list(range(1,23)),
	yticks=list(range(1,21))
).get_figure().savefig("Practica_4_lines.png")

df_barh = pd.DataFrame({ 'Drivers': df['Driver'], 'Mean': df['mean'] })
df_barh.plot.barh(x='Drivers', y='Mean', figsize=(14,6)).get_figure().savefig("Practica_4_barh.png")
