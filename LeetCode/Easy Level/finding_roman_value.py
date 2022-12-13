def romanToInt(self, s: str) -> int:
    value = 0
    i = 0
    while i < len(s):
        if i == (len(s)-1):
            if s[i] == 'I':
                value += 1

            if s[i] == 'V':
                value += 5
            if s[i] == 'X':
                value += 10
            if s[i] == 'L':
                value += 50
            if s[i] == 'C':
                value += 100
            if s[i] == 'D':
                value += 500
            if s[i] == 'M':
                valule += 1000
        else:
            if s[i] == 'I':
                if s[i+1] == 'V':
                    i += 1
                    value += 5
                if s[i+1] == 'X':
                    i += 1
                    value += 9
                else:
                    value += 1

            elif s[i] == 'V':
                value += 5
                
            elif s[i] == 'X':
                if s[i+1] == 'L':
                    i += 1
                    value += 40
                if s[i+1] == 'C':
                    i += 1
                    value += 90
                else:
                    value += 10

            elif s[i] == 'L':
                value += 50
            
            elif s[i] == 'C':
                if s[i+1] == 'D':
                    value += 400
                    i += 1
                if s[i+1] == 'M':
                    i += 1
                    value += 900
                else:
                    value += 100

            elif s[i] == 'D':
                value += 500
            
            elif s[i] == 'M':
                value += 1000
            
            i += 1
    return value

dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10
}
value = 0
s = 'XIV'


