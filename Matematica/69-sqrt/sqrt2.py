class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
            
        min = 1
        max = x

        while min <= max:
            meio = (min+max)//2
            if meio * meio == x:
                return meio
            elif meio * meio <= x:
                min = meio +1
            else:
                max = meio -1
        
        return max