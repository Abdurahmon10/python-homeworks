#1
a=list(input("Please enter the list:\n").split(" "))
b=input("Please enter the element:\n")
print(b,"is repeated",a.count(b),"times inside the list")

#2
a=list(map(int,input("PLease enter the list:\n").split(" ")))
print("Sum of all elements:",sum(a))

#3
a=list(map(int,input("PLease enter the list:\n").split(" ")))
print("Largest element in a is:",max(a))

#4
a=list(map(int,input("PLease enter the list:\n").split(" ")))
print("Smallest element in a is:",min(a))

#5
a=list(input("PLease enter the list:\n").split(" "))
b=input("Please enter the element:\n")
if(b in a):
    print("The given element is present in the list.")
else:
    print("The given element is not present in the list.")

#6
a=list(input("PLease enter the list:\n").split(" "))
if(not(a)):
    print("The given list is empty.")
else:
    print("The first element of the list is:",a[0])

#7
a=list(input("PLease enter the list:\n").split(" "))
if(not(a)):
    print("The given list is empty.")
else:
    print("The first element of the list is:",a[-1])


#8
a=list(input("PLease enter the list:\n").split(" "))
b=a[0:3].copy()
print("Here is the sliced listL",b)

#9
a=list(input("PLease enter the list:\n").split(" "))
b=a[::-1].copy()
print("Here is the reverseed list:",b)

#10
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=a.copy()
b.sort()
print("Here is the sorted verion of the list:",b)


#11
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=set(a)
print("Here is the verion of the list consisting of unique elements:",b)

#12
a=list(input("PLease enter the list:\n").split(" "))
b=input("Please enter the element:\n")
i=int(input("Please enter the index:\n"))
a.insert(i,b)
print("Here is the updated verion of the list:",a)


#13
a=list(input("PLease enter the list:\n").split(" "))
b=input("Please enter the element:\n")
print("Here is the index of",b,"in the list:",a.index(b))

#14
a=list(input("PLease enter the list:\n").split(" "))
if(not(a)):
    print("The given list is empty.")
else:
    print("The given has some elements")

#15
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=[i for i in a if i%2==0]
print("THe number of even elemnts:",len(b))

#16
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=[i for i in a if i%2==1]
print("THe number of odd elemnts:",len(b))

#17
a=list(input("PLease enter the list:\n").split(" "))
b=list(input("PLease enter the list:\n").split(" "))
a.extend(b)
print("Here is the merged list:",a)

#18
a=list(input("PLease enter the list:\n").split(" "))
b=list(input("PLease enter the sublist:\n").split(" "))
print(a,b)
if(any(a[i:i+len(b)] == b for i in range(len(a) - len(b) + 1))):
    print("Sublist",b,"exist in",a)
else:
    print("sublist not found")

#19
a=list(input("PLease enter the list:\n").split(" "))
b=input("Please enter the element:\n")
c=input("Please enter the pther element:\n")
a[a.index(b)]=c
print("Updated list:",a)

#20
a=list(map(int,input("PLease enter the list:\n").split(" ")))
a.sort()
print(a[-2])

#21
a=list(map(int,input("PLease enter the list:\n").split(" ")))
a.sort()
print(a[1])

#22
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=[i for i in a if i%2==0]
print("Even elemnts:",b)

#23
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=[i for i in a if i%2==1]
print("Even elemnts:",b)

#24
a=list(input("PLease enter the list:\n").split(" "))
print("List length:",len(a))

#25
a=list(input("Enter the list:\n").split(" "))
b=a.copy()
print("Here is the list a:",a,"and its address:",id(a),"and","here is the list b:",b,"and its address:",id(b))

#26
a=list(input("Enter the list:\n").split(" "))
if(len(a)%2==1):
    print("Middle element:",a[len(a)//2])
else:
    print("Middle elements:",a[len(a)//2-1],a[len(a)//2])

#27
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=int(input("Enter the beginning index of the sublist(list started from 0):\n"))
e=int(input("Enter the ending index of the sublist(list started from 0):\n"))
a1=a[b:e+1]
mx=max(a1)
print(mx)

#28
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=int(input("Enter the beginning index of the sublist(list started from 0):\n"))
e=int(input("Enter the ending index of the sublist(list started from 0):\n"))
a1=a[b:e+1]
mn=min(a1)
print(mn)

#29
a=list(input("Enter the list:\n").split(" "))
b=int(input("Enter the index:\n"))
a.pop(b)
print(a)

#30
a=list(input("Enter the list:\n").split(" "))
b=a.copy()
b.sort()
if(a==b):
    print("It is sorted.")
else:
    print("It is not sorted.")

#31
a=list(input("Enter the list:\n").split(" "))
b=int(input("Enter the index:\n"))
a1=[]
for i in a:
    for c in range(b):
        a1.append(i)
print(a1)

#32
a=list(input("PLease enter the list:\n").split(" "))
b=list(input("PLease enter the list:\n").split(" "))
a.extend(b)
a.sort()
print("Here is the merged, sorted list:",a)

#33
a=list(input("PLease enter the list:\n").split(" "))
b=input("Input the element to be found:\n")
af=[i for i in range(len(a)) if a[i]==b]
print(af)

#34
a=list(input("PLease enter the list:\n").split(" "))
b=a.copy()
b.pop()
b=b[::-1]
b.append(a[-1])
b=b[::-1]
a=b
print(a)

#35
a=int(input())
b=int(input())
l=[i for i in range(a,b+1)]
print(l)

#36
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=[i for i in a if i>0]
print(sum(b))

#37
a=list(map(int,input("PLease enter the list:\n").split(" ")))
b=[i for i in a if i<0]
print(sum(b))

#38
a=list(input("PLease enter the list:\n").split(" "))
b=a.copy()
b=b[::-1]
if(a==b):
    print("Palindrome.")
else:
    print("Not palindrome.")


39
a=list(input("PLease enter the list:\n").split(" "))
b=int(input("Enter the size of sublist:\n"))
c=[]
for i in range(0,len(a),b):
    c.append(a[i:i+b])
print(c)

#40
a=list(input("PLease enter the list:\n").split(" "))
b=list(dict.fromkeys(a))
print(b)
