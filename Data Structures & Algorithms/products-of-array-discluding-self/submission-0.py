import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        out = []
        while i < len(nums):
            prod = math.prod(nums[:i] + nums[i+1:])
            out.append(prod)
            i += 1
        return out