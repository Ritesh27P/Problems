def print_rangoli(size):
    # your code goes here
    temp = 'abcdefghijklmnopqrstuvwxyz'
    alphabets = [i for i in temp]

    width = (size + (size-1)) + (size + (size-1))//2
    height = (size*2) -1

    consider = alphabets[size-1::-1]

    initial_alphabet = 1
    for i in range(height//2):
        for j in range(width):
            print('-', end='')
        print()
    
    pattern = ""
    for i in consider:
        pattern += f"{i}-"
    for i in alphabets[1:size]:
        if i == alphabets[size-1]:
            pattern += i
            continue
        pattern += f"{i}-"


    print(pattern)


print_rangoli(3)

# print(len('c-b-a-b-c'), 'c-b-a-b-c', 3)
# print(len('e-d-c-b-a-b-c-d-e'), 'e-d-c-b-a-b-c-d-e', 5)
