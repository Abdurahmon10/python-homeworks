import pandas as pd
tasks=pd.read_json("task.json")
print(tasks)


def total_tasks(tasks):
    return(tasks.shape[0])

def completed_tasks(tasks):
    completed=0
    for i,rows in tasks.iterrows():
        if(rows["completed"]):
            completed+=1
    return completed

def pending_tasks(tasks):
    peding=0
    for i,rows in tasks.iterrows():
        if(not(rows["completed"])):
            peding+=1
    return peding

def average_priority(tasks):
    priority_sum=0
    for i,rows in tasks.iterrows():
        priority_sum+=rows["priority"]
    return priority_sum/tasks.shape[0]

def convert_csv(tasks):
    tasks_new=tasks
    tasks_new.columns=["ID","Task","Completed","Priority"]
    tasks_new.to_csv("task.csv",index=False)
    tasks_csv=pd.read_csv("task.csv")
    return tasks_csv
print(total_tasks(tasks))
print(completed_tasks(tasks))
print(pending_tasks(tasks))
print(average_priority(tasks))
print(convert_csv(tasks))

