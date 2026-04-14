
#H.W
values = [1, 1, 1, 3, 4, 4, 5, 4]
check = []

for i in values:
    if i not in check:
        rep = 0
        for j in values:
            if i == j:
                rep += 1
        check.append(i)
        if rep > 1:
            print(i, "repeated", rep, "times")