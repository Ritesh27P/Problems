def pickingNumber(a):
    unique_number = []
    combination = 0
    for i in a:
        if i not in unique_number:
            unique_number.append(i)
    unique_number = sorted(unique_number)

    temp1 = 0
    for i in unique_number:
        if i+1 in unique_number:
            temp1 += (a.count(i) + a.count(i+1))
            unique_number.remove(i+1)
        
        if combination < temp1:
            combination = temp1
        temp1 = 0

    return (combination)


print(pickingNumber([1, 1, 2, 2, 4, 4, 5, 5, 5]))
print(pickingNumber([1, 2, 2, 3, 1, 2]))
print(pickingNumber([5, 6, 5, 3, 3, 1]))
print(pickingNumber([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]))