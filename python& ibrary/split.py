fullname = "mayar Asad"
firstname=fullname.split()[0]
secondname=fullname.split()[1]

print(firstname)
print(secondname)

import re
text="SpiltStringBYUbber"
result= re.split("(?=[A-Z])",text)
print(result)

width,length,height=map(int,input("enter the width and length and highe: ").split())

print(width)
print(length)
print(height)