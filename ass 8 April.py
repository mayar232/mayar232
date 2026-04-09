while True:
    examNum = int(input("How many exam grades does each student have? "))

    total = 0

    for exam in range(1, examNum + 1):
        grade = float(input("Exam " + str(exam)))
        total =total + grade

    ave = total / examNum
    print("The average is", ave)

    repeat = input("Is there another student? (Y/N): ")
    repeat.lower()

    if repeat == "n":
        break