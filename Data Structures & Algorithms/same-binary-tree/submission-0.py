# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        equal = True
        def dfs(pNode,qNode):
            nonlocal equal
            if not equal:
                return
            if pNode and not qNode:
                equal = False
                return
            if not pNode and qNode:
                equal = False
                return
            if not pNode and not qNode:
                return
            if pNode.val!=qNode.val:
                equal = False
                return 
            dfs(pNode.left,qNode.left),dfs(pNode.right,qNode.right)
        dfs(p,q)
        return equal