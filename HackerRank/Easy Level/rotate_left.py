def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        arr.append(arr[i])
    print(arr)
    for i in range(d):
        arr.pop(0)
    
    return arr

def rotateLeft(d, arr):
    for _ in range(d):
        arr.append(arr[0])
        arr.pop(0)
        print(arr)
    return arr

print(rotateLeft(4, [1, 2, 3, 4, 5]))