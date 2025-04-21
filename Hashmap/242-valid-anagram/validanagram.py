class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for char in s:
            freq[char] = 1 + freq.get(char,0)

        for char in t:
            if char not in s:
                return False 
            elif freq[char] == 0:
                return False
            else:
                freq[char] -= 1

        return True