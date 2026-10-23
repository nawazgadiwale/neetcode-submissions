class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        
        
        res.sort(key=lambda x: nums.count(x), reverse=True)
        return res[:k]
