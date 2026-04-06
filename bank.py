user=input("enter the user: ")
passw=input("enter the password: ")
username="admin"
password="1234"
balance=2000
choice=input("choose option: 1,2,3: ")



if user==username and passw==password:
        print ("1.check balance")
        print ("2.deposit money")
        print ("3.withdraw money")
        if choice=="1":
         print(" your balance is:" ,balance)
        elif choice=="2":
            amount=float(input("enter the deposit money: " ))
          
            print("your new balance is: " ,balance+amount)
        elif choice=="3":
             amount=float(input("enter the withdraw money: " ))
             if amount<=balance:
          
                 print("the new balance is: ",balance- amount)
             else:
                 print("the money is not enough")
        
        else:
            print("invalid choice")
  
            
else:
    print("access denied")
    
    