# At the annual meeting of Board of Directors of Acme Inc. 
# If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?


# Brute forse algorithm
def handshake(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
    sum = 0
    for i in range(1, n):
        sum += i
    return sum


print(handshake(5))

def handshake(n):
    if n < 1:
        return 0
    return n-1 + handshake(n-1)

print(handshake(5))