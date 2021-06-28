import csv

with open('class1.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
totalmarks=0
m=len(filedata)
for marks in filedata:
    totalmarks+=float(marks[1])
mean=totalmarks/m
print("mean is :"+str(mean))

import pandas as pv
import plotly.express as pe
df=pv.read_csv("class1.csv")
fig=pe.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=mean,
        y1=mean,
        x0=0,
        x1=m
    )
])
fig.update_yaxes(rangemode="tozero")
fig.show()