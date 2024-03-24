class Solution:
    def isValid(self, s: str) -> bool:
        mydic = {")":"(", "}":"{", "]":"["}
        stack = []
        
        if s[0] in mydic: # key is close parentheses
            return False
        
        for par in s:
            if par in mydic.values(): # open parentheses
                stack.append(par)
            else: 
                if stack and stack[-1] == mydic[par]:  # stack last item의 mydic[par] 가 같다면
                    stack.pop()
                else:
                    stack.append(par)
        
        if len(stack) == 0:
            return True
        return False
            
            

            
            

            
        
        