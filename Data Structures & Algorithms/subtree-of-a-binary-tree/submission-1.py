# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root is subRoot
        def isSameTree(p,q):
            if not p or not q:
                return p is q
            return (p.val == q.val
                    and isSameTree(p.left, q.left)
                    and isSameTree(p.right, q.right))
        pos=root
        def find(node):
            if not node:
                return False
            return isSameTree(node, subRoot) or find(node.left) or find(node.right)
        
        return find(root)