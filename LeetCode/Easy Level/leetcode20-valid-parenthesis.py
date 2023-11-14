class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for i in s:
            if len(stack) == 0:
                if i in map.keys():
                    return False
                stack.append(i)
            else:
                if i in map.keys():
                    if stack[-1] == map[i]:
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)


        if len(stack) == 0:
            return True
        return False
                    
                

        
        
            
            
            
            


                


