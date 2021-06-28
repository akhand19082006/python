import pandas as pd
import plotly.express as ps
df=pd.read_csv("marks.csv")
fig=ps.scatter(df,x="Days Present",y="Marks In Percentage")
fig.show()