#Solution 1
bigDic = {'Ali': {'Math': 85, 'Science': 78, 'English': 92},
          'Sara': {'Math': 90, 'Science': 88, 'English': 85}}
subjectsDic = {}
for stdName, innerDic in bigDic.items():
    print(stdName, innerDic)
    
    for subject, grade in innerDic.items():
        if subject not in subjectsDic:
            subjectsDic[subject] = 0
        subjectsDic[subject] = subjectsDic[subject] + grade
for sub1, totalGrade in subjectsDic.items():
    print(sub1, "the average is: ", totalGrade/len(bigDic))


###################################
    
records=  [{'Math': 85, 'Science': 78, 'English': 92},
           {'Math': 90, 'Science': 88, 'English': 85}]

averages = {}

for subject in records[0]:
    total = 0
    
    for record in records:
        total=total+record[subject]
    
    avg = total / len(records)
    averages[subject] = avg

print(averages)
#######solution2:

records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]
result = {}
subjects = {}
for name, subject, mark in records:
    if name not in result:
        result[name] = {}
    result[name][subject] = mark
    if subject not in subjects:
        subjects[subject] = []
    subjects[subject].append(mark)
for name in result:
    total = sum(result[name].values())   
    count = len(result[name])            
    avg = total / count                 
    print(name,"grade average", avg)
for subject in subjects:
    total = sum(subjects[subject])      
    count = len(subjects[subject])      
    avg = total / count                 
    print(subject,"averge mark", avg)
