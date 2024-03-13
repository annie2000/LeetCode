# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         row, col = len(matrix), len(matrix[0])
        
#         topR, botR = 0, row-1
#         # midR = (topR + botR)//2
        
#         while topR <=botR:
#             midR = (topR + botR)//2
#             if target < matrix[midR][0]:
#                 botR = midR -1
#             elif target > matrix[midR][-1]:
#                 top = midR + 1
#             else:
#                 break
        
#         if not(topR<=botR):
#             return False
        
#         l, r = 0, col-1
#         midR = (topR + botR)//2
        
#         while l <= r:
#             mid = (l+r)//2
#             if target < matrix[midR][mid]:
#                 r = mid -1
#             elif target > matrix[midR][mid]:
#                 l = mid + 1
#             else:
#                 return True
#         return False
                
            
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        
        topR, botR = 0, row-1
        
        while topR <= botR:
            midR = (topR + botR) // 2
            if target < matrix[midR][0]:
                botR = midR - 1
            elif target > matrix[midR][col-1]:
                topR = midR + 1
            else:
                break
        
        if not (topR <= botR):
            return False
        
        l, r = 0, col-1
        
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[midR][mid]:
                r = mid - 1
            elif target > matrix[midR][mid]:
                l = mid + 1
            else:
                return True
        return False
