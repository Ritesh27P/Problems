# # n = 5
# # sequence = []
# # arr = []
# # if n%2 == 0:
# #     for i in range(n//2):
# #         arr.append(2)
# # else:
# #     for i in range(n//2):
# #         arr.append(2)
# #     arr.append(1)

# # print(arr)
# # for i in range(len(arr)):
# #     value = []
# #     current_sequence = []
# #     for j in range(len(arr)):
# #         value.append(arr[j])
# #         if sum(value) == n:
# #             if current_sequence not in sequence:
# #                 # print('hii')
# #                 sequence.append(current_sequence)

# # # for i in range(len(arr))
# # while 2 in arr:
# #     for i in arr:
# #         if i == 2:
# #             arr.remove(2)
# #             arr.append(1)
# #             arr.append(1)
# #             print(arr)
# #             for i in range(len(arr)):
# #                 value = []
# #                 current_sequence = []
# #                 for j in range(len(arr)):
# #                     value.append(arr[j])
# #                     if sum(value) == n:
# #                         if current_sequence not in sequence:
# #                             print('hii')
# #                             sequence.append(current_sequence)


# n = 5
# sequence = []
# arr = []
# if n%2 == 0:
#     for i in range(n//2):
#         arr.append(2)
# else:
#     for i in range(n//2):
#         arr.append(2)
#     arr.append(1)
# print(arr)
# while 2 in arr:
#     for i in arr:
#         if i == 2:
#             arr.remove(2)
#             arr.append(1)
#             arr.append(1)
#             print(arr)
#             for i in range(len(arr)):
#                 value = []
#                 current_sequence = []
#                 for j in range(len(arr)):
#                     value.append(arr[j])
#                     if sum(value) == n:
#                         if current_sequence not in sequence:
#                             print('hii')
#                             sequence.append(current_sequence)




n = 5
arr = []
sequence = []
value = 0

for i in range(n//2):
    arr.append(2)
if n%2 == 1:
    arr.append(1)

while 2 in arr:
    print(arr, sequence)
    sequence.append(arr)
    arr.remove(2)
    arr.append(1)
    arr.append(1)

print(sequence)


