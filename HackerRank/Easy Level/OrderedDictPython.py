# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

temp = int(input())

my_dict = OrderedDict()

for i in range(temp):
    temp_list = input().split()
    item = ''
    for i in temp_list[:-1]:
        item += i + " "
    
    if item in my_dict.keys():
        my_dict[item] = my_dict[item] + int(temp_list[-1])
    else:
        my_dict[item] = int(temp_list[-1])
    

for i in my_dict.keys():
    print(f"{i}{my_dict[i]}")