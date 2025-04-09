class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        palavra_letra = {}
        letra_palavra = {}
        for i in range(len(s)):
            if (pattern[i] in palavra_letra and palavra_letra[pattern[i]] != s[i]) or (s[i] in letra_palavra and letra_palavra[s[i]] != pattern[i]):
                return False
            elif pattern[i] not in palavra_letra:
                palavra_letra[pattern[i]] = s[i]
                letra_palavra[s[i]] = pattern[i]
                

        return True
      