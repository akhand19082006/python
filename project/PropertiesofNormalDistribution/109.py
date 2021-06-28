import csv
import plotly.figure_factory as pf
import pandas as pd
import statistics
df=pd.read_csv("data.csv")
mean=statistics.mean(df["reading score"].tolist())
standarddeviation=statistics.stdev(df["reading score"].tolist())
median=statistics.median(df["reading score"].tolist())
mode=statistics.mode(df["reading score"].tolist())
sumr=df["reading score"].tolist()
sd1start,sd1end=mean-standarddeviation,mean+standarddeviation
sd2start,sd2end=mean-(2*standarddeviation),mean+(2*standarddeviation)
sd3start,sd3end=mean-(3*standarddeviation),mean+(3*standarddeviation)
datainsd1=[result for result in sumr if result >sd1start and result <sd1end]
datainsd2=[result for result in sumr if result >sd2start and result <sd2end]
datainsd3=[result for result in sumr if result >sd3start and result <sd3end]
print(mean,"\n",standarddeviation,median,mode)
print("{}% of data lies in 1sd".format(len(datainsd1)*100.0/len(sumr)))
print("{}% of data lies in 2sd".format(len(datainsd2)*100.0/len(sumr)))
print("{}% of data lies in 3sd".format(len(datainsd3)*100.0/len(sumr)))
fig=pf.create_distplot([df["reading score"].tolist()],["Reading Score"],show_hist=True)
fig.show()