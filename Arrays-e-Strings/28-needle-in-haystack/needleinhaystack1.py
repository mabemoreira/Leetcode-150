class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        indice_needle = 0
        inicio = 0
        i = 0

        while i < len(haystack):
            if haystack[i] == needle[indice_needle]:
                indice_needle += 1
                if indice_needle == len(needle):
                    return inicio
                i += 1
            else:
                inicio += 1
                i = inicio 
                indice_needle = 0

        return -1 