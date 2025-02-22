import csv

import pandas as pd

def average(grades):
    sum=dict()
    num=dict()
    n=grades.shape[0]
    for i in range(n):
        if(grades.loc[i]["Subject"] in sum):
            sum[grades.loc[i]["Subject"]]+=int(grades.loc[i]["Grade"])
            num[grades.loc[i]["Subject"]]+=1
        else:
            sum[grades.loc[i]["Subject"]]=int(grades.loc[i]["Grade"])
            num[grades.loc[i]["Subject"]]=1
        #print(sum,"\n",num)

    averages=dict()
    for k,v in sum.items():
        print(k,v)
        averages[k]=v/num[k]
    return averages
        

      
      
      



grades=pd.read_csv("grade_manager.csv")


averages=pd.DataFrame(list(average(grades).items()),columns=["Subject","Average Grade"])
averages.to_csv("averages.csv",index=False)

average_grades=pd.read_csv("averages.csv")
print(average_grades)

