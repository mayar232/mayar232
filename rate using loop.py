rate=5.0
initialbalance=10000.0
numYears=int(input("enter the number of years: "))
balance=initialbalance
for year in range(1,numYears+1):
    interest= balance*rate/100
    balance= balance+interest
    print("%4d %10.2f" %(year,balance))