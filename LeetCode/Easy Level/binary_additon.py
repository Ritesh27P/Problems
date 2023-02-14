class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        value = ''
        if len(b) > len(a):
            a = a[::-1] + ((len(b)-len(a)) * '0')
            b = b[::-1]
        elif len(b) < len(a):
            b = b[::-1] + ((len(a)-len(b)) * '0')
            a = a[::-1]
        elif len(b) == len(a):
            print('3 if')
            b = b[::-1]
            a = a[::-1]

        for i in range(len(a)):
            tempA = int(a[i])
            tempB = int(b[i])

            if (tempA + tempB + carry) == 3:
                carry = 1
                value += '1'
            elif (tempA + tempB + carry) == 2:
                carry = 1
                value += '0'
            elif (tempA + tempB + carry) == 1:
                carry = 0
                value += '1'
            elif (tempA + tempB + carry) == 0:
                value += '0'
            # print(tempA, tempB, carry, value)

        if carry == 1:
            value += '1'
        return value[::-1]