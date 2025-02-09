import random
#1
a=set(input("Please enter the set element:\n").split(" "))
b=set(input("Please enter the other set element:\n").split(" "))
c=a|b
print(c)

#2
a=set(input("Please enter the set element:\n").split(" "))
b=set(input("Please enter the other set element:\n").split(" "))
c=a&b
print(c)

#3
a=set(input("Please enter the set element:\n").split(" "))
b=set(input("Please enter the other set element:\n").split(" "))
c=a-b
print(c)

#4
a=set(input("Please enter the set element:\n").split(" "))
b=set(input("Please enter the other set element:\n").split(" "))
if(a < b):
    print(a,"is the subset of",b)
elif(b < a):
    print(b,"is the subset of",a)
else:
    print("no subsets")

#5
a=set(input("Please enter the set element:\n").split(" "))
b=input("Input the element to be found:\n")
if(b in a):
    print("found")
else:
    print("Not found")

#6
a=set(input("Please enter the set element:\n").split(" "))
print(len(a))

#7
a=list(input("PLease enter the list:\n").split(" "))
b=set(a)
print(b)

#8
a=set(input("Please enter the set element:\n").split(" "))
b=input("Input the element to be removed:\n")
if(b in a):
    a.remove(b)
print(a)

#9
a=set(input("Please enter the set element:\n").split(" "))
a.clear()
print(a,len(a))


#10
a=set(input("Please enter the set element:\n").split(" "))
if(len(a)==0):
    print("it is empty")
else:
    print("it is not empty")

#11
a=set(input("Please enter the set element:\n").split(" "))
b=set(input("Please enter the other set element:\n").split(" "))
c=a-b
d=b-a
e=c|d
print(e)


#12
a=set(input("Please enter the set element:\n").split(" "))
b=input("Input the element to be added:\n")
if(not(b  in a)):
    a.add(b)
print(a)

#13
a=set(input("Please enter the set element:\n").split(" "))
x=a.pop()
print(x)

#14
a=set(map(int,input("Please enter the set element:\n").split(" ")))
print(max(a))

#15
a=set(map(int,input("Please enter the set element:\n").split(" ")))
print(min(a))

#16
a=set(map(int,input("Please enter the set element:\n").split(" ")))
b=set(i for i in a if i%2==0)
print(b)

#17
a=set(map(int,input("Please enter the set element:\n").split(" ")))
b=set(i for i in a if i%2==1)
print(b)

#18
b=int(input("Enter the start index:\n"))
e=int(input("Enter the end index:\n"))
a=set(i for i in range(b,e+1))
print(a)

#19
a=list(input("Please enter the list element:\n").split(" "))
b=list(input("Please enter the other list element:\n").split(" "))
c=set(a+b)
print(c)

#20
a=set(input("Please enter the set element:\n").split(" "))
b=set(input("Please enter the other set element:\n").split(" "))
c=a&b
if(len(c)==0):
    print("no elements in common.")
else:
    print("there areelements in common.")

#21
a=list(input("Please enter the list element:\n").split(" "))
b=list(set(a))
print(b)

#22
a=list(input("Please enter the list element:\n").split(" "))
print(len(set(a)))

#23
b=int(input("Enter the start index:\n"))
e=int(input("Enter the end index:\n"))
n=int(input("Enter the size of the set"))
a = set(random.sample(range(b, e+1), n))
print(a)  

