import math 
import csv
with open ("C-PROJECT105-MAIN/data1.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#step1:calculating the mean 
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean 

#step2:squaring and getting the values
squared_list=[] 
for number in data :
    a=int(number)-mean(data)
    a=a ** 2
    squared_list.append(a)

#step3:getting sum
sum=0
for i in squared_list:
    sum=sum+i

#step4:dividing the sum by total values
result=sum/(len(data)-1)

#step5:getting the standard deviation by taking square root of the result
std_deviation=math.sqrt(result)
print(std_deviation)