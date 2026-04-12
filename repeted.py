values=[1,1,1,3,4,4,5,4]
for i in range(len(values)):
    for m in range(i+1,len(values)):

        if values[i]==values[m]:
           
            print(values[i],values[m]) 
         
values = [1,1,1,3,4,4,5,4]
check=[]

for i in values:
    if i not in check:
     check.append(i)

for x in check:
    value=values.count(x)
    print(x, "repeated", value, "times")