# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good=0
        def bfs(maxval,root):
            nonlocal good
            if not root:
                return
            if root.val>=maxval:
                good+=1
            maxval=max(maxval,root.val)
            l,r=bfs(maxval,root.left),bfs(maxval,root.right)
        bfs(-101,root)
        return good
            
                
            