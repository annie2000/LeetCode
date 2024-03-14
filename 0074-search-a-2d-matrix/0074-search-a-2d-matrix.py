class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])* len(matrix) -1

        while l <= r:
            m = (l + r) //2
            ele = matrix[m//len(matrix[0])][m % len(matrix[0])]
            if target < ele:
                r = m -1
            elif target > ele:
                l = m + 1
            else:
                return True
        
        return False 
            
        
        
            