class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        
        for r in range(len(s)): # r is index
            while s[r] in seen: # already the character[l] has been inserted. : S[r] is the same character as s[l]
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            res = max(res, r-l+1)
        
        return res
        