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
        r = len(height) -1
        
        while l<r:
            tempAW = min(height[l], height[r]) * (r-l)
            maxAW = max(tempAW, maxAW)
            if height[l] >= height[r]:
                r -=1
            else:
                l +=1
        return maxAW
        
        
        