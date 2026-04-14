records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]

dictt={}
for name,sub,grade in records:
    if name not in dictt:
        dictt[name]={}
    dictt[name][sub]=grade
print(dictt)


records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]
print("-------")
dictt={}
for record in range(len(records)):
    name=records[record][0]
    sub=records[record][1]
    grade=records[record][2]
    if name not in dictt:
        dictt[name]={}
    dictt[name][sub]=grade
print(dictt)

print("----------")

records={
         {'Math': 85, 'Science': 78, 'English': 92},
         {'Math': 90, 'Science': 88, 'English': 85}
         }
student={}
for record in range(len(records)):
    name=records[record][1]
    sub=records[record][2]
    grade=records[record][3]
    if name not in student:
        student[name]={}
    student[name][sub]=grade
    total=0
    avg = total / len(subjects)
    print(student,avg)
    
    
    


        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
## Expected output
#{
    #"Ali": {"Math": 85, "Science": 78, "English": 92},
    #"Sara": {"Math": 90, "Science": 88, "English": 85}
#}