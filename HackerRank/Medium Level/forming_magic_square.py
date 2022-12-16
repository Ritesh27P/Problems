# def formingMagicSquare(s):
#     # Write your code here
#     for i in range(len(s)):
#         if sum(s[i]) != 15:
#             print(s[i])
#             for j in range(3):
#                 column_sum = 0
#                 for k in range(3):
#                     column_sum += s[j][k]
#                 print(column_sum)



# print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))


# arr1 = [x for x in range(1, 10)]
# print(arr1)

# temp1 = []
# for i in arr1:
#     for j in arr1:
#         for k in arr1:
#             if (i+j+k) == 15 and i != j != k != i:
#                 temp1.append([i, j, k])

# # print(temp1)
# temp2 = []
# for i in temp1:
#     if i[1] == 5:
#         print(i)
#         i1 = sorted(i)
#         if i1 not in temp2:
#             # print(i)
#             temp2.append(i1)

# # print(temp2)

allComb = ['618753294', '816357492', '834159672', '438951276', '672159834', '276951438', '294753618', '492357816']

def to_string(arr):
    word = ''
    for i in arr:
        for j in i:
            word += str(j)

    return word


word = to_string([[5, 3, 4], [1, 5, 8], [6, 4, 2]])

close_matching = 0
close_matching_word = ''

for i in allComb:
    matching_figure = 0
    for j in range(len(i)):
        if i[j] == word[j]:
            matching_figure += 1
    if close_matching < matching_figure:
        close_matching = matching_figure
        close_matching_word = i

cost = 0
for i in range(len(word)):
    if word[i] != close_matching_word[i]:
        cost += abs(int(word[i]) - int(close_matching_word[i]))

print(cost)

def f1(s):
    word = ''
    for i in s:
        for j in i:
            word += str(j)
    
    allComb = ['618753294', '816357492', '834159672', '438951276', '672159834', '276951438', '294753618', '492357816']

    close_matching_number = 0
    close_matching_word = ''

    for i in allComb:
        temp1 = 0
        for j in range(len(i)):
            if word[j] == i[j]:
                temp1 += 1
        if close_matching_number < temp1:
            close_matching_number = temp1
            close_matching_word = i
    
    cost = 0
    for i in range(len(word)):
        if word[i] != close_matching_word[i]:
            cost += abs(int(word[i]) - int(close_matching_word[i]))
    
    return cost

print(f1([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))
print(f1())
    