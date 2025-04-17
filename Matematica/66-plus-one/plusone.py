class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ao_contrario = digits[::-1]

        for i in range(len(ao_contrario)):
            if ao_contrario[i] != 9:
                ao_contrario[i] += carry
                carry = 0
                break

            else:
                carry = 1
                ao_contrario[i] = 0

        if carry:
            ao_contrario.append(1)

        return ao_contrario[::-1]