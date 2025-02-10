open("employees.txt","a")

def add_record():
    


while True:
    user_choice=int(input("Choose a number from one to six for a corresponding action:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit"))
    while user_choice<1 or user_choice>6:
        user_choice=int(input("Please enter an available option:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit"))
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
        delet_record()
        continue
    if(user_choice==6):
        break

    