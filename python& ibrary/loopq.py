
inputStr=input("enter a value or empty string to stop: ")
nagativecount=0

while inputStr != "":
    num = int(inputStr)
    
    if num < 0:
        nagativecount= nagativecount+ 1
    inputStr=input("enter a value or empty string to stop: ")
    
   

print("Number of negative values:", nagativecount)

    
    