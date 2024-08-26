a = [1, 2, 2, 4, 5, 5, 9, 9, 7]

count_dict = {}
for num in a:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

b = [num for num in count_dict if count_dict[num] == 2]
print(count_dict)
print(b)
