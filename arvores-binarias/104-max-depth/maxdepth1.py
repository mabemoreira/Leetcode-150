from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nivel = 0
        if root is None:
            return 0
        fila = deque([root])
        while fila:
            for i in range(len(fila)):
                no = fila.popleft()
                if no.left:
                    fila.append(no.left)
                if no.right:
                    fila.append(no.right)
            nivel+=1
        return nivel
