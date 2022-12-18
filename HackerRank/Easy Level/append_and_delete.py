def appendAndDelete(s, t, k):
    error_spot = 0
    if len(s) <= len(t):
        for i in range(len(s)):
            if len(t) == i+1:
                error_spot = i+1
                break
            if s[i] != t[i]:
                error_spot = i
                break
    else:
        error_spot = i+1
        # error_spot = i + 1
    # print(s[error_spot:], t[error_spot:])
    if (len(s[error_spot:]) + len(t[error_spot:])) > k:
        return "NO"
    return "YES"

     



print(appendAndDelete(['a', 'b', 'c'], ['d', 'e', 'f'], 6))
print(appendAndDelete(['a', 's', 'h', 'l', 'e', 'y'], ['a', 's', 'h'], 2))
print(appendAndDelete(['a', 'b', 'a'], ['a', 'b', 'a'], 7))
print(appendAndDelete(['h','a','c','k','e','r','h','a','p','p','y'], ['h','a','c','k','e','r','r', 'a', 'n', 'k'], 9))
print(appendAndDelete(['r', 'i', 't'], ['r', 'i', 't', 'e', 's', 'h'], 5))