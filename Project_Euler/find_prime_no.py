def next_prime(n, list):
    while True:
        temp = 0
        for i in list:
            if n%i == 0:
                n += 1
                break
            temp += 1
        if temp == len(list):
            return n


def n_prime(n):
    prime_no1 = [2, 3, 5]
    if n < 4:
        return prime_no1[n-1]
    for i in range(3, n):
        prime_no1.append(next_prime(prime_no1[-1] +1, prime_no1))
    # print(prime_no1)
    return prime_no1[-1]

print(n_prime(10001))
