# def save_prisnor(n, m, s):
#     candy = m
#     current_chair = s
#     while True:
#         if candy == 1:
#             return current_chair
#         candy -= 1
#         if current_chair == n:
#             current_chair = 1
#         else:
#             current_chair += 1
        
# print(save_prisnor(5, 2, 1))
# print(save_prisnor(3, 7, 3))
# print(save_prisnor(7, 19, 2))
    

# def save_prisnor(n, m, s):
#     candy = m 
#     current_chair = s

#     while True:
#         if candy == 1:
#             return current_chair
#         candy -=1
#         if current_chair == n:
#             current_chair = 1
#         else:
#             current_chair += 1

# print(save_prisnor(7, 19, 2))

def save_prisnor(n, m, s):
    cp = s-1
    if n > m:
        for i in range(m):
            cp += 1
            if cp == n+1:
                cp = 1
        return cp
    
    for i in range(s, m, n-1):
        # print('cp = ', i)
        cp = i

    temp = m - cp + 1
    return temp


print(save_prisnor(7, 19, 2))
print(save_prisnor(3, 7, 3))
print(save_prisnor(5, 2, 1))
print(save_prisnor(5, 2, 2))