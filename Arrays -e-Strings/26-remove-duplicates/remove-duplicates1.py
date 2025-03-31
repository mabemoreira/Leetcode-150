class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        freq = { i : 0 for i in set(nums)}
        for j in range(len(nums)):
            if freq[nums[j]] == 0:
                nums[i] = nums[j]
                freq[nums[j]] = 1
                i += 1
        return i