class Employee:

    def __init__(self,Id,Name,Position,Salary):
        self.Id=Id
        self.Name=Name
        self.Position=Position
        self.Salary=Salary
    def __str__(self):
        return self.Id+", "+self.Name+", "+self.Position+", "+str(self.Salary)+"\n"

class EmployeeManager:


    def __init__(self,filename):
        self.filename=filename
        self.ids=[]
        self.employees_dict={
            "":Employee("","","",0.0)
            }

    def fill_dict(self):
        with open(self.filename,"r") as employees:
            for record in employees:
                employee_details=record.split(", ")
                employee=Employee(employee_details[0],employee_details[1],employee_details[2],round(float(employee_details[3]),3))
                self.employees_dict.update({employee_details[0]:employee})
        
    def add_record(self):
        employees=employees=open(self.filename,"a")
        employeeId=input("Enter employee Id to be added:\n")
        while employeeId in self.ids:
            employeeId=input("Already exists, enter another one:\n")
        employeeName=input("Enter employee Name to be added:\n")
        employeePosition=input("Enter employee Position to be added:\n")
        employeeSalary=float(input("Enter employee Salary to be added:\n"))
        employee=Employee(employeeId,employeeName,employeePosition,employeeSalary)
        employees.write(str(employee))
        employees.close()
        self.ids.append(employeeId)
        self.employees_dict.update({employeeId:employee})

    def view_records(self):
        sort_choice=int(input("Sort using: 1. id, 2. name(A-z), 3. Position(A-z), 4.Salary(ascending or descending)(enter the choice number):\n "))
        while sort_choice<0 or sort_choice>4:
            sort_choice=int(input("Sort using: 1. id, 2. name(A-z), 3. Position(A-z), 4.Salary(ascending or descending)(enter the choice number):\n "))
        if(sort_choice==1):
            self.employees_dict=dict(sorted(self.employees_dict.items(), key=lambda item: item[1].Id))
        if(sort_choice==2):
            self.employees_dict=dict(sorted(self.employees_dict.items(), key=lambda item: item[1].Name))
        if(sort_choice==3):
            self.employees_dict=dict(sorted(self.employees_dict.items(), key=lambda item: item[1].Position))
        if(sort_choice==4):
            a_d=input("Enter a for ascending and d for descending:\n")
            while a_d.lower()!="a" and a_d.lower()!="d":
                a_d=input("Enter a for ascending and d for descending:\n")
            if a_d=="d":
                self.employees_dict=dict(sorted(self.employees_dict.items(), key=lambda item: item[1].Salary, reverse=True))
            else:
                self.employees_dict=dict(sorted(self.employees_dict.items(), key=lambda item: item[1].Salary))
        print("Employee ID, Name, Position, Salary\n")
        for k , v in self.employees_dict.items():
            if(k!=""):
                print(v)


        #with open(self.filename,"r") as file:
         #   for line in file:
          #      print(line)

    def search_employee(self):
        while True:
            employeeId=input("Please enter employee ID to search for :\n")
            with open(self.filename,"r") as employees:
                for line in employees:
                    employee_details=line.split(", ")
                    employee=Employee(employee_details[0],employee_details[1],employee_details[2],employee_details[3])
                    if(employee.Id==employeeId):
                        print("Name:\n",employee.Name)
                        print("Position:\n",employee.Position)
                        print("Salary:\n",employee.Salary)
                        employees.close()
                        return True
            print("Employee not found!")

    def  update_info(self):
        employeeId=input("Please enter employee ID to search for :\n")
        records=[]
        with open(self.filename,"r") as employees:
            records=employees.readlines()
            employee_found=False
        with open(self.filename,"w") as employees:
            for line in records:
                employee_details=line.split(", ")
                employee=Employee(employee_details[0],employee_details[1],employee_details[2],employee_details[3])
                if(employee.Id==employeeId and not(employee_found)):
                    new_id=input("Input updated Id( or enter - for no change):\n")
                    while new_id in self.ids and new_id!="-":
                        new_id=input("Input updated Id, another one( or enter - for no change):\n")
                    if(new_id!="-"):
                        employee.Id=new_id

                    new_name=input("Input updated name( or enter - for no change):\n")
                    if(new_name!="-"):
                        employee.Name=new_name
                        
                    new_position=input("Input updated position( or enter - for no change):\n")
                    if(new_position!="-"):
                            employee.Position=new_position
                        
                    new_salary=float(input("Input updated salary( or enter - for no change):\n"))
                    if(new_salary!="-"):
                        employee.Salary=round(new_salary,3)
                        

                    if(new_id!="-"):
                        employeeId=new_id
                    self.employees_dict[employeeId]=employee

                    employee_found=True
                    employees.write(str(employee))
                else:
                    employees.write(line)
        if(not(employee_found)):
            choice=input("Employee not found.\n Try again?(enter yes)\n")
            if choice.lower()=="yes":
                self.update_info()
                        

    def delete_record(self):
        employeeId=input("Please enter employee ID to search for :\n")
        self.ids.remove(employeeId)
        records=[]
        with open(self.filename,"r") as employees:
            records=employees.readlines()
        employee_found=False
        with open(self.filename,"w") as employees:
            for line in records:
                employee_details=line.split(", ")
                employee=Employee(employee_details[0],employee_details[1],employee_details[2],employee_details[3])
                if(employee.Id!=employeeId):
                    employees.write(line)
                else:
                    employee_found=True
                    del self.employees_dict[employeeId]
        if(not(employee_found)):
            choice=input("Employee not found.\n Try again?(enter yes)\n")
            if choice.lower()=="yes":
                self.delete_record()
        
    def menu(self):
        try:
            employees=open(self.filename,"r")
        except FileNotFoundError:
            employees=open(self.filename,"a")
            #employees.write("Employee ID, Name, Position, Salary\n")
            employees.close()
        self.fill_dict()
        while True:
            user_choice=int(input("Choose a number from one to six for a corresponding action:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n"))
            while user_choice<1 or user_choice>6:
                user_choice=int(input("Please enter an available option:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\n"))
            if(user_choice==1):
                self.add_record()
                continue
            if(user_choice==2):
                self.view_records()
                continue
            if(user_choice==3):
                self.search_employee()
                continue
            if(user_choice==4):
                self.update_info()
                continue
            if(user_choice==5):
                self.delete_record()
                continue
            if(user_choice==6):
                return True
            
record_manager=EmployeeManager("employees.txt")
if(record_manager.menu()):
    print("Bye...")







     
