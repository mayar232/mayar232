count=0
number=input("Eenter a number: ")
total=0
while count<len(number):
    total=total +int(number[count])
    count=count+1
print(total)  