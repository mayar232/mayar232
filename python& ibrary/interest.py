rate=5
balance=10000
target=20000
year=0
while balance<=target:
    year=year+1
    intrest=balance*rate/100
    balance=balance+intrest
    print(year,balance)