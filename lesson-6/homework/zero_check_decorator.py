def check(func):
    def wrapper(a,b):
        if(b==0):
            print("Denominator can't be zero")
            return None
        return func(a,b)
    return wrapper

@check
def div(a, b):
   return a / b

a=int(input("Enter the numerator:\n"))
b=int(input("Enter the denominator:\n"))
q=div(a,b)
if(q!=None):
    print(q) 
            
            

