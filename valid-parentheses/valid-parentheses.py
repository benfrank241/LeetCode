class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        map = {")": "(", "}": "{", "]": "["}
        
        for b in s:
            
            if (b == '(' or b == '[' or b == '{'):
                stack.append(b)
            
            else:
                top = stack.pop() if stack else '#'
                
                if map[b] != top:
                    return False
        
        return not stack
            

        