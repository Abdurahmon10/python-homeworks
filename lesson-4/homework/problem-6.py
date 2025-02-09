def is_prime(a):
    i=2
    while(i*i<=a):
        if(a%i==0):
            return False
        i+=1
    
    return True

for i in range(101):
    if(is_prime(i)):
        print(i)
