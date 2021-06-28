import pandas as pd
import plotly.express as ps
import statistics
import csv
df=pd.read_csv("data2.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig=ps.scatter(mean,x="student_id",y="level",color="attempt",size="attempt")
fig.show()