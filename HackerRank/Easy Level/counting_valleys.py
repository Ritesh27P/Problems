def countingValleys(steps, path):
    valleys = 0
    sea_level = 0
    valley_start = False

    for i in path:
        if i == 'U':
            sea_level += 1
            if sea_level > 0:
                continue
            if sea_level == 0 and valley_start:
                valleys += 1
                valley_start = False
        
        if i == 'D':
            sea_level -= 1
            if sea_level < 0:
                valley_start = True
    
    return valleys
            

print(countingValleys(8, 'UDDDUDUU'))


