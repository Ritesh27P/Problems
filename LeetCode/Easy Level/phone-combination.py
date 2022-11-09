

def letterCombinations(digits):
    d1 = {
        "2": ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    combination = []

    for i in digits:
        l1 = []
        for j in d1[i]:
            l1.append(j)
        combination.append(l1)
    
    for i in combination:
        word = ''
        for j in i:
            word += j
        print(word)

            

    return combination

print(letterCombinations('23'))
        



