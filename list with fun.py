friend=['ali','muna','ahamed','reem','malake']
friend. insert (1,"mayar")
print(friend)
print("--------")

friend=['ali','muna','ahamed','reem','malake']
if "ali" in friend:
    print(" in list")
else:
        print("not found")
print("_____________")

friend=['ali','muna','ahamed','reem','malake']
n=friend.index("muna")
print(n)
print("_____________")
friend=['ali','muna','ahamed','reem','malake']
friend.pop(2)
print(friend)
print("_--------")

friend=['ali','muna','ahamed','reem','malake']
friend.remove("ali")
print(friend)
print("--------")

myfriend=["mayar","noor"]
friend=["ahmad","sara"]
ourfriend=myfriend+friend
print(ourfriend)
print("______________")

myfriend=["mayar","noor"]*2

print(myfriend)
#############
def multible(lis,factor):
    
    lis=list(lis)
    for i in range(len(lis)):
        lis[i]=lis[i]*factor
    return lis
listt=[1,2,3]
factor=2
print(multible(listt,factor))
print(listt)
################################
temretures=[18,21,33,32,44,39,40,39,36,30,22,18]
print (len(temretures))
fourquarater=temretures[:6]
print(fourquarater)



matrix=[
            [2,4,5,1],
            [3,2,9,6],
            [1,0,2,10],
            ]
totals=[]

for row in range(len(matrix)):
    total=0
    for j in range (len(matrix[row])):
            total=total+matrix[row][j]
    totals.append(total)
maxx=max(totals)
print(totals.index(20))
        