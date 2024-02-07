class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        cnt = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            cnt[s[r]] = 1 + cnt.get(s[r], 0)
            
            
            while r - l + 1 - max(cnt.values()) >k:
                cnt[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
        return res
                
        