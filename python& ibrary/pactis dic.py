dic={
    "sunday":[30,29],
    "monday":[29,31],
    "tuesday":[31,30],
    "wedensday":[33,32],
    "thursday":[35,33],
    "friday":[28,30],
    "saturday":[25,23]
    }


totalTemp=0
for day,temp in dic.items():
    print(day,temp[1])
    
    totalTemp =  totalTemp + temp[1]
aveTemp = totalTemp / len(dic)
print(" the avreag temp is : ",aveTemp)

print("-----------------------------")

dic={
    "sunday":[30,29],
    "monday":[29,31],
    "tuesday":[31,30],
    "wedensday":[33,32],
    "thursday":[35,33],
    "friday":[28,30],
    "saturday":[25,23]
    }

for day in dic.keys():
    user=int(input("enter the temp for week 3 and -1 to stop : "))
    dic[day].append(user)
print(dic)
print("-----------------------------")

###################_______________________________
dic["sunday"].append(31)
dic["monday"].append(35)
dic["tuesday"].append(30)
dic["wedensday"].append(34)
dic["thursday"].append(36)
dic["friday"].append(27)
dic["saturday"].append(24)

print(dic)
print("-----------------------------")
#__________________________________________________
week3Temp=[33,22,34,26,25,31,32]
dic["sunday"].append(week3Temp[0])
dic["monday"].append(week3Temp[1])
dic["tuesday"].append(week3Temp[2])
dic["wedensday"].append(week3Temp[3])
dic["thursday"].append(week3Temp[4])
dic["friday"].append(week3Temp[5])
dic["saturday"].append(week3Temp[6])

print(dic)
index=0
for day in dic.keys():
        dic[day].append(week3Temp[index])
        index+=1
print(dic)

    

     
    
