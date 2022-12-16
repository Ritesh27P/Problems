def permutation_equation(s):
    prob = []
    temp = []
     
    for i in range(0, len(s)):
        temp.append((i+1, s[i]))

    for i in range(len(s)):
        for j in temp:
            if j[1] == i+1:
                # print(j[0])
                px = j[0]
                for k in temp:
                    if k[1] == px:
                        prob.append(k[0])
    return prob
    
permutation_equation([5, 2, 1, 3, 4])
