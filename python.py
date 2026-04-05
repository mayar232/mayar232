cans_per_pack=6
userInput=input("please enter the price for a six-pack: ")
packprice=float(userInput)
userInput=input("please enter the volume for each can (in ounces): ")
canvolume=float(userInput)
packvolume=canvolume*cans_per_pack
pricePerounce=packprice/packvolume
print("price per ounce: %8.2f" %pricePerounce)


