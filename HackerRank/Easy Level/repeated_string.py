def repeated_string(s, n):
    if len(s) == 1:
        if s == 'a':
            return n
    if 'a' not in s:
        return 0
    new_s = ''
    for i in range(n//len(s)):
        new_s += s

    for i in range(n%len(s)):
        new_s += s[i]
    print(new_s)

    return new_s.count('a')


print(repeated_string('aba', 10))

def repeated_string(s, n):
    if 'a' not in s:
        return 0
    if s == 'a':
        return n
    if s == 'aa':
        return n//2
    if s == 'aaa':
        return n//3
    a_count = s.count('a')

    value = 0
    value += a_count * (n//len(s))
    value += s[0:n%len(s)].count('a')

    return value

print(repeated_string('aba', 10))
print(repeated_string('a', 1000000000))
