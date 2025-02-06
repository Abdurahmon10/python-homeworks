#1
username=input()
password=input()
if(username=="" and password==""):
    print("both are empty")
elif (username=="" and password!=""):
    print("username is empty")
elif(username!="" and password!=""):
    print("password is empty")
else:
    print("both username and password was entered")

#2
a=int(input())
b=int(input())
if(a==b):
    print(a,'is equal to',b)
else:
    print("they are not equal")

#3
a=int(input())
if(a>0 and a%2==0):
    print(a,"is positive and even.")
else:
    print("The number is either negative or odd.")

#4
a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c):
    print("all of the are the same")
elif(a==b and b!=c or a!=b and b==c):
    print("two of them are the same")
else:
    print("all of them are different")

#5
string1=input()
string2=input()
if(len(string1)!=len(string2)):
    print("string lengths are the same")
else:
    print(string1,"and",string2,"have different lengths")


#6
a=int(input())
if(a%5==0 and a%3==0):
    print(a,"is divisible by both 3 and 5.")
else:
    print(a," is not divisible by either 3 or 5.")

#7
a=int(input())
b=int(input())
if(a+b>50):
    print("their sum is bigger than 50")
else:
    print("their sum is not bigger than 50")

#8
a=int(input())
if(a>=10 and a<=20):
    print(a,"is inside the given range of 10 to 20 inclusive")
else:
    print(a,"is not between 10 and 20.")