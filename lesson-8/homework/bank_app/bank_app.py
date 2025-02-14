import datetime
from random import randint
try:
    file=open("accounts.txt","r")
    file.close()
except FileNotFoundError:
    file=open("accounts.txt","a")
    file.close()

rand_id=[]
for i in range(10000):
    rand_id.append(str(i))

class Account:
    def __init__(self,id,name,balance,password):
        self.__name=name
        if(id=="-1"):
            self.__id=rand_id[0]
            rand_id.pop(0)
        else:
            self.__id=id
        self.__balance=balance
        self.__password=password
        self.__deposits=[]
        self.__withdrawals=[]
    def deposit(self):
        verification=self.check_pass()
        if(not(verification)):
            print("not verified")
            return False
        try:
            amount=int(input("Enter the amount:\n"))
        except TypeError:
            return False
        self.__balance+=amount
        self.__deposits.append({"amount":amount,"date":datetime.datetime.now()})
        return True
    def withdrawal(self):
        verification=self.check_pass()
        if(not(verification)):
            print("not verified")
            return False

        try:
            amount=int(input("Enter the amount:\n"))
        except ValueError:
            return False
        chances=10
        while amount>self.__balance and chances>0:
            try:
                print("Balance is",self.__balance,". Enter the amount:\n")
                amount=int(input())
                chances-=1
            except TypeError:
                return False
        if(chances==0):
            return False
        else:
            self.__balance-=amount
            self.__withdrawals.append({"amount":amount,"date":datetime.datetime.now()})
            return True

    @property
    def balance(self):
        return self.__balance
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return  f"{self.__id}, {self.__name}, {self.__balance}, {self.__password}"
    
    def check_pass(self):
        password=input("enter the password")
        chances=5
        while(password!=self.__password and chances>0):
            password=input("enter the password")
            chances-=1
        if(chances):
            return True
        else:
            return False
        


    def change_password(self):
        verification=self.check_pass()
        if(not(verification)):
            print("not verified")
            return False
        new_pass=input("Enter new password(four digits):\n")
        chances=5
        while (len(new_pass)>4 or len(new_pass)==0 )and chances>0:
            new_pass=input("Enter new password(four digits):\n")
            chances-=1

        if(chances):
            self.__password=new_pass
            return True
        return False
    

class Bank:
    def __init__(self,filename):
        self.__accounts=dict()
        self.__filename=filename
    
    def load(self):
        with open(self.__filename,"r") as file:
            for line in file:
                line_details = [x.strip() for x in line.split(",")]
                #print(line_details)
                id=line_details[0]
                name=line_details[1]
                balance=line_details[2]
                password=line_details[3].strip()
                account=(Account(id,name,int(balance),password))
                self.__accounts[account.id]=account
    def display(self):
        for k,v in self.__accounts.items():
            print("for",v.name," we have:\t")
            print("Id:",k)
            print("Balance:",v.balance)
            print("-"*30)
    def deposit(self,id):
        if(self.__accounts[id].deposit()):
            print("deposited successsfullt.")
        else:
            print("smth went wrong")
    def withdrawal(self,id):
        if(self.__accounts[id].withdrawal()):
            print("Withdrawal was successful.")
        else:
            print("smth went wrong.")

    def add_account(self,id,name,balance,password):
        with open(self.__filename,"a") as file:
            account=Account(id,name,balance,password)
            self.__accounts[account.id]=account
            file.write(str(account)+"\n")
            
            print("account successfully created with id:",account.id)
    def remove_account(self,id):
        deleted=self.__accounts.pop(id,None)
        
        if(deleted!=None):
            print(deleted.id,"was deleted.")
        else:
            print("None was deleted.")




my_bank=Bank("accounts.txt")
my_bank.load()

while True:
    #menu
    print("1.Display accounts.\n2.Add account.\n3.Remove account.\n4.Deposit.\n5.Withdraw.\n6.exit")
    user_choice=int(input("Enter a choice betwee 1-7 for the choices given:\n"))
    if(user_choice==1):
        my_bank.display()
    
    elif(user_choice==2):
        name=input("enter name of the owner:\n")
        password=input("Enter a four character word for the password:\n")
        while len(password)==0 or len(password)>4 and password!="--":
            password=input("Enter a four character word for the password again of -- for termination:\n")
        if(password=="--"):
            print("creation terminated")
        else:
            my_bank.add_account("-1",name,0,password)
    elif(user_choice==3):
        id=input("Enter id to be removed:\n")
        my_bank.remove_account(id)

    elif(user_choice==4):
        id=input("Enter id to deposit in:\n")
        my_bank.deposit(id)
        #amount=int(input("enter the amount:\n"))
        #account=my_bank.finder(id)
        #account.dep
    elif(user_choice==5):
        id=input("Enter id to withdraw from:\n")
        my_bank.withdrawal(id)

    elif(user_choice==6):
        break
    else:
        print("wrong choice.try again.")

    



        
    







