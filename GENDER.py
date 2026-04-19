major = input("please enter your major: ")
gender = input("please enter your gender: ")

major = major.lower()
gender = gender.lower()

if "eng" in major:
    if "fem" in gender:
        print("you are a wonderful girl engineering")
    else:
        print("you are eng but not female")
else:
    print("you are not engineering")
    
           
           
           
