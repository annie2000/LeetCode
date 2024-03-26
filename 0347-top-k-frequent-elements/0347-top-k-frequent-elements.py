class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydic = collections.defaultdict(int)
        res = []
        
        for num in nums:
            if not mydic[num]:
                mydic[num] = 0
            mydic[num] +=1
            
        # mydic ={1:2, 2:3, 3: 1, 4: 4}
        
        sortD = sorted(mydic.values())[::-1] # [4, 3, 2, 1] -> index -> 4:0, 3:1, 2: 2, 1: 3
        #print(sortD)
        
        for key in mydic:
            if mydic[key] >= sortD[k-1]:
                res.append(key)
        return res
            
            
        