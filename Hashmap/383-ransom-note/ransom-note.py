class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in magazine:
            freq[i] += 1
        for i in ransomNote:
            if(freq[i] == 0):
                return False
            freq[i] -= 1    
        return True