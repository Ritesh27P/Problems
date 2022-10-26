def pageCount(n, p):
    # Write your code here
    start_flip_pages = 0;
    for i in range(0, n+1, 2):
        if i == p or i+1 == p:
            break
        else:
            start_flip_pages += 1
    
    end_flip_pages = 0;
    for i in range(n, 0, -2):
        if i==p or i-1 == p:
            break
        else:
            end_flip_pages += 1;
    
    return min(start_flip_pages, end_flip_pages)


print(pageCount(6, 2))
print()
print(pageCount(5, 4))