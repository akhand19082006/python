import math
import csv


with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata[0]
def mean(data):
    totalmarks=0
    m=len(data)
    for marks in data:
        totalmarks += int(marks)
    mean=totalmarks/m
    return mean
squarelist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squarelist.append(a)
sum=0
for i in squarelist:
    sum=sum+i
result=sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)
