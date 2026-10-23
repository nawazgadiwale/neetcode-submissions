class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        for i in nums:
            if nums.count(i)>1 and i in seen:
                return True
                break
        else:
            return False
