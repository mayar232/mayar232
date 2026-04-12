username = "admin"
password = "1234"
balance = 2000

def display():
    return(balance)
def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("deposit succsesful")
def withdraw():
    global balance
    amount = float(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("withdraw sucsseful")
    else:
        print("Not enough balance")
    


while True:
    user = input("Enter username: ")
    passw = input("Enter password: ")
    
    if user == username and passw == password:
        print("Login is successful")
        break  
    else:
        print("Wrong username or password, try again")

print("1. Check balance")
print("2. Deposit money")
print("3. Withdraw money")

choice = input("Choose option 1, 2, 3, or q to quit: ")

while choice != "q":
    if choice == "1":
        print("Your balance is:", display())

    elif choice == "2":
        deposit()
        print("Your new balance is:",display())

    elif choice == "3":
            withdraw()
            print("Your new balance is:", display())
       
    else:
        print("Invalid choice")
        
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")

    choice = input("Choose option 1, 2, 3, or q to quit: ")
