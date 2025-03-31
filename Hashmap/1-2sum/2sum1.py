class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resp = []
        cand = {num: i for i, num in enumerate(nums)}  
        for i, num in enumerate(nums):
            dif = target - num
            if dif in cand and cand[dif] != i: 
                resp.append(i)
                resp.append(cand[dif])
                break
        return resp