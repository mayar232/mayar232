listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
add = []
for i in range(1):
    add.append(listt[1])
    add.append("mayar")

    for j in range(1,len(listt)):
        add.append(listt[j])
    print(add)
    #######################
listt = ["Ali","Muna","Ahmed","Reem","Nuha"]
add = []

add.append("mayar")

for i in listt:
    if i not in add:
        add.append(i)

print(add)
