#shape 1
for line in range (5):
    for i in range(line + 1) :
        print("*","",end="")
    print()
    
#shape 2
for line in range(5,0,-1):
    for i in range(line):
        print("* ", end="")
    print()

#shape 6
for line in range (5):
    for i in range(5) :
        print("*","",end="")
    print()


#shape 7
for line in range(1, 6):
    print("* " * line)

for line in range(4, 0, -1):
    print("* " * line)
    
    