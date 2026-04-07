prev = 0
num = input("Enter a number or empty string to stop: ")
while num != "":
    prev = int(num)
    num = int(input("Enter a number or empty string to stop: "))
    if num == prev:
        print ("This is adjacent to the previous input") 