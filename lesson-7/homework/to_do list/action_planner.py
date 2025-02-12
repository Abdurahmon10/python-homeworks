import csv
import json
from abc import ABC, abstractmethod

class Storage_Manager(ABC):
    @abstractmethod
    def load_tasks(self):
        pass
    def save_tasks(self,tasks):
        pass
    def add_tasks(self,tasks):
        pass

class CSV_storage(Storage_Manager):
    def __init__(self,filename="tasks.csv"):
        self.filename=filename
    def load_tasks(self):
        tasks=[]
        try:
            with open(self.filename,newline='',mode="r") as file:
                reader=csv.DictReader(file)
                for row in reader:
                    tasks.append(row)
        except FileNotFoundError:
            pass
        return tasks
    def save_tasks(self,tasks):
        with open(self.filename,newline="",mode="w") as file:
            fields=["Id", "Title", "Description", "Deadline","Status"]
            writer=csv.DictWriter(file,fieldnames=fields)
            writer.writeheader()
            writer.writerows(tasks)
    def add_task(self,task):
        tasks=self.load_tasks()
        tasks.append(task)
        self.save_tasks(tasks)


class JSON_storage(Storage_Manager):
    def __init__(self,filename="tasks.json"):
        self.filename=filename
    def load_tasks(self):
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_tasks(self,tasks):
        with open(self.filename,"w") as file:
            json.dump(tasks,file,indent=4)
    def add_task(self, task):
       tasks=self.load_tasks()
       tasks.append(task)
       self.save_tasks(tasks)

def get_storage(storage_type):
    if(storage_type=="json"):
        return JSON_storage()
    elif storage_type=="csv":
        return CSV_storage()
    else:
        raise("Invalid storage type")


class TaskManager():
    def __init__(self,storage :Storage_Manager):
        self.storage=storage
        self.tasks=self.storage.load_tasks()
    
    def add_task(self,id,title,description,deadline,status):
        new_task={
            "Id":id,
            "Title":title,
            "Description":description,
            "Deadline":deadline,
            "Status":status

        }
        self.tasks.append(new_task)
        self.storage.save_tasks(self.tasks)
        print("Task added!\n")
    
    def list_tasks(self):
        if not self.tasks:
            print("Empty list.")
        else:
            for task in self.tasks:
                print(task)
    def remove_task(self,task_id):
        task_id = str(task_id)  
        original_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["Id"] != task_id]

        if len(self.tasks) < original_length:
            self.storage.save_tasks(self.tasks)
            print("Task deleted successfully!\n")
        else:
            print("Task ID not found!\n")



storage_format=input("Input storage format(either csv or json):\n")
storage=get_storage(storage_format)
manager=TaskManager(storage)

#menu

while(True):
    user_choice=input("Choose what you want to do with your to do list:\n1. Add task\n2. View tasks\n3. Delete task\n4. Exit\n")
    if(user_choice=="1"):
        id=input("Input Id:\n")
        title=input("Input title:\n")
        description=input("Input description:\n")
        deadline=input("Input deadline:\n")
        status=input("Input status:\n")
        manager.add_task(id,title,description,deadline,status)
    elif(user_choice=="2"):
        manager.list_tasks()
    elif(user_choice=="3"):
        id=input("Input Id(of the task that you wanna remove):\n")
        manager.remove_task(id)
    else:
        break



        



        

    


            





        
        
    

