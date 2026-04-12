num = [2, 3, 4, 5, 6, 7]
num.sort()
number=int(input("Enter a number: "))

for i in range(len(num)):
    if num[i] == number:
        print("index:", i)
        break
else:
    print("out of list")
print("---------")    
    
def is_leap(year):
    if (year%4==0 and year%100!=0 )or year%400==0:
        return True
    else:
            return False
print(is_leap(2020))