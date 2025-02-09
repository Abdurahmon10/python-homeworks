a=list(input("Enter the first list:\n").split())
b=list(input("Enter the second list:\n").split())
c=[]
for i in a:
    if(not(i in b)):
        c.append(i)
for i in b:
    if(not(i in a)):
        c.append(i)

print(c)
