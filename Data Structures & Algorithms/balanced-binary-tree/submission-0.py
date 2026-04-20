# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return 0  # Height of empty subtree
            
            left = check(node.left)
            if left == -1:
                return -1  # Left subtree not balanced
            
            right = check(node.right)
            if right == -1:
                return -1  # Right subtree not balanced
            
            if abs(left - right) > 1:
                return -1  # Current node not balanced
            
            return max(left, right) + 1  # Height of current subtree
        
        return check(root) != -1