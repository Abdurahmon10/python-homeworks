#1
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=input("Please enter the element to be found:\n")
print(b,"appear in this tuple",a.count(b),"time(s).")

#2
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
print("Max:",max(a))

#3
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
print("Min:",min(a))

#4
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=input("Please enter the element to be found:\n")
if(a.count(b)>0):
    print(b,"is there.")
else:
    print(b,"is not there.")

#5
a=tuple(input("PLease enter the tuple:\n").split(" "))
if(not(a)):
    print("It is empty.")
else:
    print(a[0])

#6
a=tuple(input("PLease enter the tuple:\n").split(" "))
if(not(a)):
    print("It is empty.")
else:
    print(a[len(a)-1])


#7
a=tuple(input("PLease enter the tuple:\n").split(" "))
print(len(a))

#8
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=a[:3]
print(b)

#9
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=tuple(input("PLease enter the other tuple:\n").split(" "))
c=a+b
print(c)

#10
a=tuple(input("PLease enter the tuple:\n").split(" "))
if(not(a)):
    print("It is empty.")
else:
    print("It is not empty.")

#11
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=input("Please enter the element to be found:\n")
l=[i for i in range(len(a)) if a[i]==b]
print(l)

#12
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
b=list(a)
b.sort()
print(b[-2])


#13
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
b=list(a)
b.sort()
print(b[1])

#14
b=input("Please enter the element to be found:\n")
a=tuple(b)
print(a)

#15
a=list(input("PLease enter the list:\n").split(" "))
b=tuple(a)
print(b)

#16
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
b=list(a)
b.sort()
b=tuple(b)
if(b==a):
    print("It is sorted.")
else:
    print("It is not sorted.")

#17
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
b=int(input("Enter the start index:\n"))
e=int(input("Enter the end index:\n"))
c=a[b:e+1]
print(max(c))


#18
a=tuple(map(int,input("PLease enter the tuple:\n").split(" ")))
b=int(input("Enter the start index:\n"))
e=int(input("Enter the end index:\n"))
c=a[b:e+1]
print(min(c))

#19
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=input("Enter the element to be removed:\n")
c=a[:a.index(b)]+a[a.index(b)+1:]
print(c)

#20
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=int(input("Size of the subtuplse:\n"))
c=tuple(a[i:i+b] for i in range(0,len(a),b))
print(c)

#21
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=int(input("Number of reps:\n"))
c=[]
for i in a:
    for j in range(b):
        c.append(i)
c=tuple(c)
print(c)

#22
b=int(input("Enter the start index:\n"))
e=int(input("Enter the end index:\n"))
a=tuple(i for i in range(b,e+1))
print(a)

#23
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=a[::-1]
print(b)

#24
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=a[::-1]
if(a==b):
    print("palindrome")
else:
    print("not palindrome")

#25
a=tuple(input("PLease enter the tuple:\n").split(" "))
b=tuple(dict.fromkeys(a))
print(b)