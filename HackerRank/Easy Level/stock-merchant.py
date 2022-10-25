def sockMerchant(n, ar):
    arr1 = []
    pair = 0
    for i in ar:
        if i in arr1:
            arr1.remove(i)
            pair += 1
        else:
            arr1.append(i)
    
    return pair