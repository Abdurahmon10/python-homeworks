import re
import sqlite3
import requests
from bs4 import BeautifulSoup
import pandas as pd

html_doc=requests.get("https://realpython.github.io/fake-jobs/").text

soup=BeautifulSoup(html_doc,"html.parser")



#print(job_titles,organizations)
#print(locations)

application_links=[i.attrs["href"] for i in soup.find_all("a") if i.text=="Apply"]
#print(application_links)

jobs=pd.DataFrame(columns=["Job Title","Organization","Location","Description","Application Link"])

gg=0

for i in application_links:
    html_doc_job=requests.get(i).text
    #print(i)
    soup_job=BeautifulSoup(html_doc_job,"html.parser")
    headers=soup_job.find_all("h1")
    job_title=""
    for header in headers:
        if len(header.attrs.keys())>0 and header.attrs["class"]==['title', 'is-2']:
            job_title=re.sub(r'\s+', ' ', header.text).strip()
            #print(i.text)
            break
    #print(job_title)
    organization=soup_job.find("h2").text
    paragraphs=soup_job.find_all("p")
    #print(paragraphs)
    location=""
    description=""
    for at in paragraphs:
        #print(at.attrs)
        if len(at.attrs.keys())==0:
            description=description = re.sub(r'\s+', ' ', at.text).strip()
        elif "id" in at.attrs.keys() and at.attrs["id"]=="location":
            location=re.sub(r'\s+', ' ', at.text).strip()
            location=re.sub(r'Location: ', '', location).strip()
        
        
    jobs.loc[len(jobs)]=[job_title,organization,location,description,i]
    #if(gg==10):
        #break
    #gg+=1

    
    




conn=sqlite3.connect("jobs.db")

c=conn.cursor()

c.execute(""" create table jobs(
          Title text,
          Organization text,
          Location text,
          Description text,
          Link text)""")

data_to_insert = [
    (row["Job Title"], row["Organization"], row["Location"], row["Description"], row["Application Link"])
    for _, row in jobs.iterrows()
]

c.executemany(
    """INSERT INTO jobs ("Title", "Organization", "Location", "Description", "Link") 
       VALUES (?, ?, ?, ?, ?)""",
    data_to_insert
)

c.execute("""select * from jobs""")
print(c.fetchall())


choice=input("1. Location 2. Company name:\n")

if(choice=="1"):
    location=input("Input location:\n")
    filtred_df=jobs[jobs["Location"==location]]
    jobs.to_csv(f"{location}.csv")
elif choice=="2":
    organization=input("Input organization:\n")
    filtred_df=jobs[jobs["Organization"]==organization]
    jobs.to_csv(f"{organization}.csv")
    

conn.commit()

conn.close()