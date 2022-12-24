def is_prime(n):
    if n == 2 or n==3 or n==5:
        return True
    if n%2 == 0:
        return False
    if n%3 == 0:
        return False
    if n%5 == 0:
        return False
    else:
        return True

def factor(n):
    largest = 0
    temp_i = 0
    if is_prime(n):
        return n
    for i in range(n):
        for j in range(n):
            if (i*j) == n:
                if j == temp_i:
                    break
                if largest < max(i, j):
                    largest = max(i, j)
                temp_i = i

    return largest

# print(factor(100))
# print(factor(13195))


# print(is_prime(13))

def number(n):
    if n%2 == 0:
        return 'even'
    if n%3 == 0:
        return 'odd'
    if n%5 == 0:
        return 'odd'
    return 'prime'

def factor(n):
    if n%2 == 0:
        return n//2
    if n%3 == 0:
        return n//3
    if n%5 == 0:
        return n//3
    return n

# print(factor(13195))
# print(factor(7))
# print(factor(10))

def factor(n):
    factors = []
    print(n)
    if is_prime(n):
        factors.append(n)
        return 
    if n%2 == 0 and n%3== 0:
        factors.append(2)
        factors.append(3)
        factor(n//2), factor(n//3)
    if n%2 == 0:
        factors.append(2)
        factor(n//2)
    if n%3 == 0:
        factors.append(3)
        factor(n//3)
    if n%5 == 0:
        factors.append(5)
        factor(n//5)
    return factors


def largest_prime_factor(n):
  # Divide n by 2 until it becomes odd
  while n % 2 == 0:
    n = n / 2
  # n is now odd
  # If n is 1, then it has no prime factors other than itself
  if n == 1:
    return 1
  # Otherwise, the largest prime factor of n is at least 3
  factor = 3
  # Divide n by increasing odd numbers until it can't be divided anymore
  while n != 1:
    while n % factor == 0:
      n = n / factor
    # If n is now 1, then factor is the largest prime factor
    if n == 1:
      return factor
    # Otherwise, try the next odd number
    factor += 2
  return factor

prime_numbers = [2, 3, 5]

n = 500001

for i in range(7, n//2+1):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    prime_numbers.append(i)
# print(prime_numbers)

largest_prime = 0
while True:
    for i in prime_numbers:
        if n%i==0:
            n /= i
            if i > largest_prime:
                largest_prime = i
            # print(n)
            break
    if n == 1:
        break

print(largest_prime)

def largest_prime_factor(n):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17]
    for i in range(15, n+1):
        if i%2==0 or i%3==0 or i%5==0:
            continue
        prime_numbers.append(i)

    largest_prime = 0
    while True:
        for i in prime_numbers:
            if n%i==0:
                n /= i
                if i > largest_prime:
                    largest_prime = i
                break
        
        if n == 1:
            break
    return largest_prime

print(largest_prime_factor(7))

