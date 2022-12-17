def jumpingOnClouds(c, k):
    energy = 100
    current_cloud = 0
    while True:
        current_cloud += k
        if current_cloud >= len(c):
            current_cloud = 0
            if c[current_cloud] == 1:
                energy -= 2
            energy -= 1
            break
        if c[current_cloud] == 1:
            energy -= 2
        energy -= 1

def jumpingONClouds(c, k):
    energy = 100

    for i in range(0, len(c), k):
        # print(i)
        if c[i] == 1:
            energy -= 3
        else:
            energy -= 1

    if c[0] == 1:
        energy -= 3
    else:
        energy -= 1
    
    return energy

c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2

c = [0, 0, 1, 0]
k = 2

print(jumpingONClouds(c, k))