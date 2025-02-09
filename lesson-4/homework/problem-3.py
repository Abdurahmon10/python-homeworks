a=input("Input the string:\n")
b=""
c="auioe"
ii=0
for i in range(0,len(a)):
    if(not(a[i] in c) and i>=ii+2 and i!=len(a)-1):
        b=b+a[i]+"_"
        c=c+a[i]
        ii=i+1
    else:
        b=b+a[i]
    #print(b,c,ii)
print(b)        
    
