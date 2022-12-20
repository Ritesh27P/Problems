# st = 1
# st2 = 2
# st3 = 3
# sum = 2
# for i in range(10):
#     st3 = st + st2
#     st, st2= st2, st3
#     if st3 >= 45:
#         break
#     if st3%2 == 0:
#         sum += st3
#         print(st3)
# print(sum)

# n = 10

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))

n = 10
st1 = 1
st2 = 2
st3 = 3
arr1 = [1, 2]
for i in range(0, n//2):
    st3 = st1 + st2
    st1, st2 = st2, st3
    if st3 >= n:
        break
    arr1.append(st3)
    
arr1 = [i for i in arr1 if i%2==0]
print(arr1)
