class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {i:0 for i in set(nums)}
        i = 0
        for j in range(len(nums)):
            if freq[nums[j]] < 2:
                freq[nums[j]] += 1
                nums[i] = nums[j]
                i += 1
        return i