# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or  not node2:
                return False
            if node1.val != node2.val:
                return False
            return issame(node1.left, node2.left) and issame(node2.right,node1.right )
        
        if not root:
            return False
        
        if issame(root, subRoot):
            return True
        # Otherwise, recursively check:
        # 1. left subtree
        # 2. right subtree
        # If either contains subRoot → return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        