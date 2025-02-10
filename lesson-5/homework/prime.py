def is_prime(n):
    i=2
    while(i*i<n):
        if(n%i==0):
            return False
        i+=1
    return True
n=int(input("Enter a positive integer:\n"))
if(is_prime(n)):
    print(n,"is prime.")
else:
    print(n,"is not prime.") 
