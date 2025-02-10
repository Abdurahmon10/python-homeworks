def invest(amount, rate, years):
    for i in range(1,years+1):
        amount*=(1+rate)
        print("year ",i,": ","{:.2f}".format(round(amount,2)),sep="")

principal_amount=float(input("Enter the principal amount:\n"))
percentage_rate=float(input("Enter the percentage rate of increase:\n"))
years=int(input("Enter the number of years:\n"))
invest(principal_amount,percentage_rate/100,years)