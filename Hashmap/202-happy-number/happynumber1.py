class Solution:
    def isHappy(self, n: int) -> bool:
        visitados = set()

        while n not in visitados:
            visitados.add(n)
            n = sum(int(c)**2 for c in str(n))
            if n == 1:
                return True

        return False
