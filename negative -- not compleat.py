inputStr = input("Enter a value or empty string to stop: ")
negativecount = 0

while inputStr != "":

    if inputStr.isdigit():
        num = int(inputStr)
        if num < 0: 
            negativecount= negativecount+ 1
    else:
        print("invalid input try again")
    
    inputStr = input("Enter a value or empty string to stop: ")

print("Number of negative values:", negativecount)