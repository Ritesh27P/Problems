def viralAdvertising(n):
    total_cult = 5//2
    cult = 5//2
    for i in range(n-1):
        produce = cult * 3
        cult = produce//2
        total_cult += cult
    return total_cult

print(viralAdvertising(5))

def rec(n):
    if n < 1:
        return 1
    