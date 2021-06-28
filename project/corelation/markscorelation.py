import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    Present=[]
    Percentage=[]
    with open(data_path) as csv_file:
        csvreader=csv.DictReader(csv_file)
        for row in csvreader:
            Present.append(float(row["Days Present"]))
            Percentage.append(float(row["Marks In Percentage"]))
    return{"x":Present,"y":Percentage}
def corelation(datasource):
    corelationvalue=np.corrcoef(datasource["x"],datasource["y"])
    print("corelation Between no. of days present and percentage of marks: \n",corelationvalue[0,1])
def setup():
    data_path="marks.csv"
    datasource=getDataSource(data_path)
    corelation(datasource)

setup()
