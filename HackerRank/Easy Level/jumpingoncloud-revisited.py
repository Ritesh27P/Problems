
def jumpingOnClouds(c):
    current_position = 0
    energy = 0
    
    while current_position < len(c)-2:
        if current_position+1 == len(c):
            energy += 1
            return energy
        if c[current_position+2] == 1:
            current_position += 1 
        else:
            current_position += 2
        energy += 1
    
    return energy

def jumpingOnClouds(c):
    pointer = 0
    energy = 0

    while True:
        if pointer+1 == len(c):
            return energy +1
        if pointer+2 == len(c):
            if c[pointer+1] == 1:
                return energy +1
