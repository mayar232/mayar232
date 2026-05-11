username = "admin"
password = "1234"
balance = 2000


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

choice = input("Choose option 1, 2, 3: ")


if choice == "1":
    print("Your balance is:", balance)

elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Your new balance is:", balance)

elif choice == "3":
    amount = float(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Your new balance is:", balance)
    else:
        print("Not enough balance")

else:
    print("Invalid choice")
    