#1
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=input("Enter the key to be found:\n")

try:
    value=a[b]
except KeyError:
    value="Not Found"

print(value)

#2
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=input("Enter the key to be found:\n")

try:
    value=a[b]
except KeyError:
    value="Not Found"

if(value!="Not Found"):
    print("Key exists.")
else:
    print("Key does not exist.")

#3
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
print(len(a))

#4
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=a.keys()
print(b)

#5
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=a.values()
print(b)

#6
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
print(a|b)


#7
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=input("Enter the key to be deleted:\n")

try:
    del a[b]
except KeyError:
    b="Not Found"

print("Deleted key:",b)
print(a)

#8
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
a.clear()
print(a)

#9
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
if(len(a)!=0):
    print("there is smth in ti:",a)
else:
    print("empty")

#10
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=input("Enter the key to be found:\n")

try:
    value=a[b]
except KeyError:
    value="Not Found"

print(b,":",value)

#11
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=input("Enter the key to be updated:\n")
c=input("Enter the value:\n")
a[b]=c

print(b,":",a[b],"\n",a)

#12
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
c=input("Enter the value:\n")
print(list(a.values()).count(c))

#13
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
b=dict(zip(a.values(),a.keys()))
print(b)

#14
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
c=input("Enter the value:\n")
print([k for k , v in a.items() if v==c])

#15
a=list(input("PLease enter the keys:\n").split(" "))
b=list(input("PLease enter the values:\n").split(" "))
c=dict(zip(a,b))
print(c)

#16
a= {k: v for k, v in (input("Enter key and value: ").split() for _ in range(int(input("Enter number of items: "))))}
bb=any(isinstance(v,dict) for v in a.values())
if(bb):
    print("it is a nested dict.")
else:
    print("it is not a nested dict.")

