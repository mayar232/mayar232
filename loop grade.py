grade=0.0
total=0.0
count=0
while grade>=0:
    grade=float(input(" enter the grade of student or -1 to stop: "))
    if grade >=0.0:
        total=total+grade
        count=count+1
avg=total/count

print(avg)
        



