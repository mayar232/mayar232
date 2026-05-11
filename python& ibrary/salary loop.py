salary=0.00
total=0.00
count=0
while salary>=0:
    salary=float(input(" enter a salary or -1 to finish: "))
    if salary >=0.0:
                 total=total+salary
                 count=count+1
                 print(salary)
print(total/count)