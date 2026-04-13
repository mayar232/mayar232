
#H.W
         
values = [1,1,1,3,4,4,5,4]
check=[]
for i in values:
    rep=0
    if i not in check:
       for j in check:
            if i==j:
                rep=rep+1
        check.append(i)
        if rep>1:
        
             print(x, "repeated", value, "times")