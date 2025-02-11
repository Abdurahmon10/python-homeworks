try:
    employees=open("employees.txt","r")
except FileNotFoundError:
    employees=open("employees.txt","a")
    employees.write("Employee ID, Name, Position, Salary\n")
    employees.close()
def add_record():
    employees=employees=open("employees.txt","a")
    employeeId=input("Enter employee Id to be added:\n")
    employeeName=input("Enter employee Name to be added:\n")
    employeePosition=input("Enter employee Position to be added:\n")
    employeeSalary=input("Enter employee Salary to be added:\n")
    employees.write(employeeId+", "+employeeName+", "+employeePosition+", "+employeeSalary+"\n")
    employees.close()

def view_records():
    with open("employees.txt","r") as file:
        for line in file:
            print(line)

def search_employee():
    while True:
        employeeId=input("Please enter employee ID to search for :\n")
        with open("employees.txt","r") as file:
            for line in file:
                line_dict=dict(zip("ID,Name,Position,Salary".split(","),line.split(", ")))
                if(line_dict["ID"]==employeeId):
                    print("Name:\n",line_dict["Name"])
                    print("Position:\n",line_dict["Position"])
                    print("Salary:\n",line_dict["Salary"])
                    employees.close()
                    return True
        print("Employee not found!")

def  update_info():
    employeeId=input("Please enter employee ID to search for :\n")
    records=[]
    with open("employees.txt","r") as employees:
        records=employees.readlines()
        employee_found=False
    with open("employees.txt","w") as employees:
        for line in records:
            line_dict=dict(zip("ID,Name,Position,Salary".split(","),line.split(", ")))
            if(line_dict["ID"]==employeeId and not(employee_found)):
                new_name=input("Input updated name( or enter - for no change):\n")
                if(new_name!="-"):
                    line_dict["Name"]=new_name
                    
                new_position=input("Input updated position( or enter - for no change):\n")
                if(new_position!="-"):
                        line_dict["Position"]=new_position
                    
                new_salary=input("Input updated salary( or enter - for no change):\n")
                if(new_salary!="-"):
                    line_dict["Salary"]=new_salary
                    
                employees.write(line_dict["ID"]+", "+line_dict["Name"]+", "+line_dict["Position"]+", "+line_dict["Salary"]+"\n")
                employee_found=True
            else:
                employees.write(line)
                    

def delete_record():
    employeeId=input("Please enter employee ID to search for :\n")
    records=[]
    with open("employees.txt","r") as employees:
        records=employees.readlines()

    with open("employees.txt","w") as employees:
        for line in records:
            line_dict=dict(zip("ID,Name,Position,Salary".split(","),line.split(", ")))
            if(line_dict["ID"]!=employeeId):
                employees.write(line)
        employees.close()

    


while True:
    user_choice=int(input("Choose a number from one to six for a corresponding action:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n"))
    while user_choice<1 or user_choice>6:
        user_choice=int(input("Please enter an available option:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n"))
    if(user_choice==1):
        add_record()
        continue
    if(user_choice==2):
        view_records()
        continue
    if(user_choice==3):
        search_employee()
        continue
    if(user_choice==4):
        update_info()
        continue
    if(user_choice==5):
        delete_record()
        continue
    if(user_choice==6):
        break

    