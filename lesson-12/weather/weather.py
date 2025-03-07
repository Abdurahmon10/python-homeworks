from bs4 import BeautifulSoup

import pandas as pd
import math

file=open("weather.html","r")

html_doc=file.read()


soup=BeautifulSoup(html_doc,"html.parser")

headers=[i.text for i in soup.find_all("th")]

forecast=[i.text for i in soup.find_all("td")]

for i in range(1,len(forecast),3):
    
    forecast[i]=int(forecast[i].replace("В°C",""))
    print(forecast[i]) 


rows=[forecast[i:i+3] for i in range(0,len(forecast),3)]

week_forecast=pd.DataFrame(rows,columns=headers)
print(week_forecast)


print(week_forecast[week_forecast["Temperature"]==(max(week_forecast["Temperature"]))] )

print(week_forecast[week_forecast["Condition"]=="Sunny"] )
print(week_forecast["Temperature"].mean())


