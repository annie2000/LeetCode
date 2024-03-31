class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # maxAW = 0 
        # update maxAW -> water container store = hight * width
        # height/width will be changed -> slide window /two pointer 
        # will use two pointer -> l = 0, r = len(height)-1 
        # loop over hehgit, calculate water amount to be stored
        # tempAW = height [i] * (r - l) -> then compare maxAW: update maxAW with bigger number
        # move l, r points when 
        # return maxAW
        
        maxAW = 0
        l = 0
        r = len(height)-1
        
        while l<r:
            tempaw = min(height[l], height[r]) * (r-l)
            maxAW = max(tempaw, maxAW)
            
            if height[l]< height[r]:
                l +=1
            else:
                r -=1
        return maxAW