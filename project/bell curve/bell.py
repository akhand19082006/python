import csv
import plotly.figure_factory as pf
import pandas as pd
import statistics
df=pd.read_csv("data.csv")
fig=pf.create_distplot([df["Avg Rating"].tolist()],["Average rating of Mobile Brand"],show_hist=True)
fig.show()