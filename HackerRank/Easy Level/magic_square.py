l1 = [2, 2, 3, 4, 5]

# print(l1.count(2))

def common(list):
    common = 0
    common_number = 0

    for i in range(len(list)):
        if list.count(list[i]) > common_number:
            common_number = i
            common = list[i]
    return common

print(common(l1))
print(common([1,1,2, 4, 5, 1, 2, 2, 4, 2]))