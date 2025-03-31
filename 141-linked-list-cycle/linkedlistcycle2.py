# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lento = rapido = head 
        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

            if lento == rapido:
                return True
        return False
            
