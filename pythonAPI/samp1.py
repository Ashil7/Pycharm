l = [1, 2, 3, 5, 6]
a = []
for i in range(len(l)):
    if i == 0 or i == 3 or i == 4:
        continue
    else:
        a.append(l[i])
print(a)
