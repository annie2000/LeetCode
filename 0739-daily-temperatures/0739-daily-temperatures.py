class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # temperatures: [73,74,75,71,69,72,76,73]
        # res = [1,1,4,2,1,1,0,0]
        
        # Res setting
        # compare temperatures [i] and temperatures[i+1] => append the result to res. 
        # initiate res with the value of 0  * len(temperatures)-1
        res = [0] * len(temperatures)
        
        # Comparison
        # compare temperatures [i] and temperatures[i+1] : use stack (monotonic stack): 
        # The characteristics of stack -> value is only increasing. 
        # Append stack only if the value is the bigger than the last value of stack.
        # Append stack temperature and index as a pair as a form of list
        # the stack elements look like -> (stack[the currently most high temperature][its index]) : 
        # temperature = [73, 74]
        # stack = [73, 0] and compare -> 74 with stack[-1][0]
        # why: the value that we should return is the diff of two indexes
        
        stack = []
        
        for i, tNum in enumerate(temperatures):
            
            while stack and tNum > stack[-1][0]:
                temp, ind = stack.pop() # temp -> [73, 0]
                res[ind] = (i - ind)
            
            stack.append([tNum, i] )

        
        return res

        
        
        
        
        # Update Res values
        # if temperature[curr +1] is bigger than temperature[curr], then stack[-1] pop 
        # and update res value -> (curr +1) - (stack[-1][1]) 
        
        # Return Res (list)
        
        
        
        
        
        
        
        
        
        
        
        
        
        