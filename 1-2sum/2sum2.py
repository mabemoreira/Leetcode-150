class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in vistos:
                return [vistos[dif], i]
            vistos[num] = i
            