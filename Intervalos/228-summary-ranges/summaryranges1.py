class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        menor = nums[0]
        maior = nums[0]
        pares = {}
        resposta = []
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] + 1:
                maior = nums[i-1]
                pares[menor] = maior
                menor = nums[i]
        
        pares[menor] = nums[len(nums)-1]

        for i,j in pares.items():
            if i != j:
                resposta.append(f"{i}->{j}")
            else:
                resposta.append(str(i))

        return resposta