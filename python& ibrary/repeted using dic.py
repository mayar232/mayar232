
            
num=[1,1,2,3,4,5,6]
repsdiv={}
for i in num:
    if i not in repsdiv:
        repsdiv[i]=num.count(i)
        print(repsdiv)