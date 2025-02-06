#1

a=float(input())
a=round(a,2)
print(a)

#2

a=int(input())
b=int(input())
c=int(input())
print('min: ',min(a,b,c),"\nmax: ",max(a,b,c))

#3
l=float(input())
print(l," kilometers is equal to: ", l*1000," meters and ", l*100000, "centimeters.")

#4
a=int(input())
b=int(input())
print("the result of division is: ",a//b,"and the remainder is ", a%b)

#5
cel=float(input())
far=cel*5/9+32
print(far)

#6
num=int(input())
print(num%10)

#7
num=int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")
