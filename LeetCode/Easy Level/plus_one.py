class Solution:
    def plusOne(self, digits):
        number = ''
        for i in digits:
            number += str(i)

        number = str(int(number) + 1)
        return [int(i) for i in number]