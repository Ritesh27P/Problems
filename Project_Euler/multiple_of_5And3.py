# sum = 0
# for i in range(5, 100, 5):
#     sum += i
# for i in range(3, 100, 3):
#     if i%5 != 0:
#         sum += i

# print(sum)


sum = 0
st = 3

#     3 5 6 9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48 50
#    3 2 1\3 1  2 \3  3  2 \1  3  1 \2  3  3 \2 1  3  1  2  3  3  2  1



#   321 312 332 131 123
sum = 0
st_value = 0
n = 10
seq = [3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3]
for _ in range(n//5):
    for i in seq:
        st_value += i
        if st_value >= n:
            break
        sum += st_value

print(sum)