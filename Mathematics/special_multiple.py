combination = ['0', '9']

temp = []
word = ''
for i in combination:
    for j in combination:
        for k in combination:
            for l in combination:
                temp.append(i+j+k+l)

print(temp)

# def recur(n):
#     for i in range(2):
