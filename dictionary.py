#dictionary

favorit={"ali":"green","adam":"red"}
print(favorit)
        ###############################
friendName={
                "Ali":[9998,7777,897],
                "muna":8976
                }
alinum=friendName["Ali"]
print(alinum)
#with index of ali:
friendName={
                "Ali":[9998,7777,897],
                "muna":8976
                }
alinum=friendName["Ali"][1]
print(alinum)
#########################################using loop
friendName={
                "Ali":[9998,7777,897],
                "muna":8976
                }
if "Ali" in friendName: 
    alinum=friendName["Ali"][0]
    print(alinum)
print(friendName.get("reem",411))

