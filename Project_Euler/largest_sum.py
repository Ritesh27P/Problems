n = int(input())

total_value = 0
for i in range(n):
    value = int(input())
    total_value += value
    
print(str(total_value)[:10])