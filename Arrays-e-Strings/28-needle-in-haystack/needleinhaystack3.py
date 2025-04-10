#NAO É MEU CÓDIGO É SAMPLE DO LEETCODE SÓ PRA VER COMO FAZER EM N² SEM SPLICING

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1
        
        for x in range(len(haystack)):
            if len(needle) > len(haystack)-x:
                return -1

            elif haystack[x] == needle[0]:
                hstart = x
                same = True
                for y in range(len(needle)):
                    if haystack[hstart] != needle[y]:
                        same = False
                    hstart += 1
                if same:
                    return x