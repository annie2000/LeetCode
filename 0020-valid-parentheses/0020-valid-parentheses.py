class Solution:
    def isValid(self, s: str) -> bool:
        
        mydic = {")":"(", "}":"{", "]":"["}
        stack = []
        
        if s[0] in mydic:
            return False
            
        for par in s:
            if par in mydic.values():
                stack.append(par) # stack = ["("]
            else: #par is one of closed parentheses
                if stack and stack[-1] == mydic[par]: # par = "]"
                    stack.pop()
                else:
                    stack.append(par)
        
        if len(stack) == 0:
            return True
        return False
                
            
                
                
                
                
                
                
                
        