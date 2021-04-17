import pandas as pd
import plotly.graph_objects as pgo
import plotly.express as pe
import csv
df=pd.read_csv("co_relation.csv")
a = df.groupby(["Marks In Percentage","Days Present"],as_index=False)["Roll No"].mean()
fig=pe.scatter(a,x="Marks In Percentage",y="Days Present",size="Roll No",color="Roll No")
fig.show()