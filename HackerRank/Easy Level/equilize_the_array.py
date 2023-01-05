def equalizeArray(arr):
    max_value = 0
    for i in arr:
        if arr.count(i) > max_value:
            max_value = arr.count(i)
    
    return len(arr) - max_value