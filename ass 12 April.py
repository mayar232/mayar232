
#LINEAR
num = [2, 3, 4, 5, 6, 7]
num.sort()
number=int(input("Enter a number: "))

for i in range(len(num)):
    if num[i] == number:
        print(i)
        break
else:
    print("out of list")
print("---------")


listt = [1,4,7,8,3]
listt.sort()
x = int(input("Enter a number: "))
start =0
end = len(listt)-1
while start<end:
    mid=(start+end)//2
    if listt[mid]==x:
        print(mid)
        break
    elif x>listt[mid]:
        start = mid + 1
    elif x<listt[mid]:
        end = mid - 1
else:
    print("Not found!")
#####################
values = [1,1,1,3,3,3]
checked = []
for i in values:
    rep = 0
    if i not in checked:
        for j in values :
            if i == j:
               rep = rep + 1
        checked.append(i)
        if rep > 1 :
            print(i, "is repeated", rep, "times")
    
def is_leap(year):
    if (year%4==0 and year%100!=0 )or year%400==0:
        return True
    else:
            return False
print(is_leap(2020))