counter=2
num=9
isprime=True

while counter <num:
    if num%counter==0:
      
        isprime=False
    counter=counter+1
print(num,isprime)

#compleat the solution سوينا لوب مرتين:
num=2
while num<200:
    counter=2
    isprime=True

    while counter <num:
        if num%counter==0:
           isprime=False
        counter=counter+1
        break
     
    if isprime:
        print("this number is prime",num)
    num=num+1
        