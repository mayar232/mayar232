fullname = "mayar Asad"
firstname=fullname.split()[0]
secondname=fullname.split()[1]

print(firstname)
print(secondname)
print("------")

import re
text="SpiltStringBYUbber"
result= re.split("(?=[A-Z])",text)
print(result)
print("------")

width,length,height=map(int,input("enter the width and length and highe: ").split())

print(width)
print(length)
print(height)
print("------") 
hour,mintue=map(int,input(" enter the time in format HH:MM: ").split(":"))
print(hour)
print(mintue)
print("------")

name,grade=input(" enter the name and grade: ").split()
print(name,grade)
