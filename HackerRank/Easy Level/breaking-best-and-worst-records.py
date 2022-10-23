def breakingRecords(scores):
    highest_score = scores[0]
    lowest_score = scores[0]
    high_change = 0
    low_change = 0
    for i in scores:
        if(i > highest_score):
            high_change += 1;
            highest_score = i;
        elif (i < lowest_score):
            low_change += 1;
            lowest_score = i;
    
    return (high_change, low_change);
