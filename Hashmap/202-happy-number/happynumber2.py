class Solution:
    def isHappy(self, n: int) -> bool:

        def calcula(n):
            total = 0
            while n:
                total += (n % 10)**2
                n = n // 10
            return total

        lento = calcula(n)
        rapido = calcula(calcula(n))

        while rapido != 1 and lento != rapido:
            lento = calcula(lento)
            rapido = calcula(calcula(rapido))

        return rapido == 1