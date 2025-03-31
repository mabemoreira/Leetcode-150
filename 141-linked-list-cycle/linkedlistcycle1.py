# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vistos = set()
        atual = head
        pos = 0
        while atual is not None:
            if atual.next is not None and atual.next in vistos:
                return True
            else:
                vistos.add(atual)
            pos += 1
            atual = atual.next
        return False