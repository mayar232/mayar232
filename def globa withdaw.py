balance=10000
def withdraw(amount):
    global balance
    if balance>=amount:
        balance=balance-amount
withdraw(350)
print("balance=",balance)