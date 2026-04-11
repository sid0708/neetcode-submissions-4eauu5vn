from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while len(queue) > 0:
            eachlevel = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    print("The value is", curr.val)
                    eachlevel.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            res.append(eachlevel)
        return res

        




        
        