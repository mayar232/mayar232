friend=['ali','muna','ahamed','reem','malake']
friend.append(" ")
x=1

for i in range (len(friend),-1,x,-1):
    friend[i]=friend[i-1]
    friend[1] = "raneem"
    print(friend)      