class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        topR = 0
        botR = len(matrix) -1
        row = (topR + botR)//2
        
        while topR <=botR:
            row = (topR + botR)//2
        
            if target < matrix[row][0]:
                botR = row -1
            elif target > matrix[row][-1]:
                topR = row + 1
            else:
                break
                
        if not(topR <=botR):
            return False
        
        l = 0
        r = col-1
        while l <= r:
            mid = (l + r)//2
            if target < matrix[row][mid]:
                r = mid -1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False
            
        
        
        
        
        