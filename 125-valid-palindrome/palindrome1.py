class Solution:
    def isPalindrome(self, s: str) -> bool:
        entrada = "".join(char for char in s if char.isalnum())
        entrada = entrada.lower()
        esq = 0
        dir = len(entrada) - 1
        while(dir > esq):
            if entrada[dir] != entrada[esq]:
                return False
            dir -= 1
            esq += 1
        return True