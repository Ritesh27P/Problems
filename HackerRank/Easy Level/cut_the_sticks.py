def cutTheSticks(arr):
    len_arr = []
    n = len(arr)
    # Write your code here
    shortest_stick = min(arr)
    for _ in range(n):
        len_arr.append(len(arr))
        for i in range(len(arr)):
            new_num = arr[i] - shortest_stick
            if new_num > 0:
                arr[i] = new_num
            else:
                arr[i] = 0
        arr = [j for j in arr if j > 0]
        if len(arr) == 0:
            return len_arr
        shortest_stick = min(arr)