t4=((1,2,3),("a","b","c"))
for j in t4:
    for k in j:
        print(k,end=" ")
        print()
t1=(1,2,1,3,4,5)
print(t1.count(1))# number 1 how many repeted
print(t1.index(1))# nimber 1 in which index
####################
numberSet={1,2,2,3,4,5,4}
print(numberSet)
print("__ _ _ _ _")
##############
emptySet={}
print(type(emptySet))
emptySet=set()
print(type(emptySet))
print("__ _ _ _ _")
########################
setWithList=set([1,2,4,1,3,4])
print(type(setWithList))
print(setWithList)
