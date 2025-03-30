from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        oposto = {')':'(', ']':'[', '}':'{'}
        pilha = deque()
        entrada = list(s)
        for i in entrada:
            if i == '(' or i == '{' or i == '[':
                pilha.appendleft(i)
            else:
                if len(pilha) == 0 or pilha[0] != oposto[i]:
                    return False
                else:
                    pilha.popleft()
        return len(pilha) == 0