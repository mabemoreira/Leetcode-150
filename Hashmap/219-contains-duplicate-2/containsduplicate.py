class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vistos = {}

        for i in range(len(nums)):
            if nums[i] in vistos:
                if(abs(vistos[nums[i]] - i) <= k):
                    return True
            vistos[nums[i]] = i

        return False 