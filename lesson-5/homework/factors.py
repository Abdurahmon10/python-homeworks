def factors(n):
    i=1
    factors_n=set()
    while(i*i<=n):
        if(n%i==0):
            factors_n.add(i)
            factors_n.add(n//i)
        i+=1
    return factors_n

n=int(input("ENter a positive number:\n"))
factors_n=factors(n)
#print(factors_n)
for i in factors_n:
    print(i,"is a factor of",n)

