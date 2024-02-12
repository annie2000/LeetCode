class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        cnt = {}
        
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) +1
            
            while r-l +1 -max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, (r-l +1))
        return res
               