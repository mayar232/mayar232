num = [4,6,5,2, 8, 9]
for i in num:
    if i % 2 == 1:
        print(i)
        
num=[-2,-3,5,4,2]
for i in range(len(num)):
    if num[i]<0:
       num[i]=0

print(num)

values=[3,2,4,6,1,0]
target=5


for i in range(len(values)):
    for m in range(i+1,len(values)):
        if values[i] + values[m] == target:
            print(values[i],values[m])        
        
# اذا اصغر بس نغير لاشارة
num = [2, 3, 4, 5, 6, 7]

maxx = num[0]  

for i in num:
    if i > maxx:
        maxx = i

print (maxx)

num=[4,6,5,2,8]
odd=num[0]
for i in num:
    if i%2==1:
        odd=i
print(odd)

    
        

      








