num = int(input("Enter a number: "))
total = 0

while num < 0:
    n = num % 10
    total = total + n
    num = num // 10

print("Sum of the digits:", total)