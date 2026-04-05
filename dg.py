from sys import exit
mark =float(input(" enter the mark: "))

if mark<0 or mark >100:

    exit(" eror you mus enter the number from 0 to 100")
    
if mark>=90:
    grade="A"
elif mark>=80:
    grade="B"
elif mark >=70:
    grade="C"
elif mark >=60:
    grade="D"
else:
     grade="F"
    
    

           