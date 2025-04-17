class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1
        while res * res <= x:
            res += 1
        return res-1