
time1 = input("Enter first time (HH:MM): ")
hour1 = int(time1[0:2])
minute1 = int(time1[3:5])

time2 = input("Enter second time (HH:MM): ")
hour2 = int(time2[0:2])
minute2 = int(time2[3:5])

if hour1 < hour2:
    print("Time 1 comes first")
elif hour1 > hour2:
    print("Time 2 comes first")
elif minute1 < minute2:
    print("Time 1 comes first")
elif minute1 > minute2:
    print("Time 2 comes first")
else:
    print("Both times are the same")