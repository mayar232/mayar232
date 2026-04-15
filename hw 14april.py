records = [
    {'Math': 85, 'Science': 78, 'English': 92},
    {'Math': 90, 'Science': 88, 'English': 85}
]

average = {}
subjects = records[0].keys() 

for subject in subjects:
    total = 0
    for record in records:
        total =total+ record[subject]
    
    avg = total / len(records)
    average[subject] = avg

print(average)


###################################
    
records=  [{'Math': 85, 'Science': 78, 'English': 92},
           {'Math': 90, 'Science': 88, 'English': 85}]

averages = {}

for subject in records[0]:
    total = 0
    
    for record in records:
        total += record[subject]
    
    avg = total / len(records)
    averages[subject] = avg

print(averages)
