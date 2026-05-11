########################
friendName={
                "Ali":9998,
                "muna":8976
                }
for key in friendName:
    print(key,friendName[key])
    
 ##################################################   
friendName = {
    "Ali": [9998, 7777, 897],
    "muna": 8976
}

for key in friendName:
    if type(friendName[key]) is list:
        count = 1
        for i in friendName[key]:
            print(key, i, count)
            count += 1
    else:
        print(key, friendName[key])
##############################
friendName = {
    "Ali": [9998, 7777, 897],
    "muna": 8976
}

for item in friendName.items():
    print(item[0],item[1])
    if type(item[1])is list:
        for i in item[1]:
            print(i)
            
            ###############
friendName = {
    "Ali": [9998, 7777, 897],
    "muna": 8976
}

for value in friendName.values():           
       print(value)

for key in friendName.key():
    print(key)