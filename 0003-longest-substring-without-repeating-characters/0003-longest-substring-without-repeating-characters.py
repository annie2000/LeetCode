class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            
            
            res = max(r-l+1, res)
        return res
        
        
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)