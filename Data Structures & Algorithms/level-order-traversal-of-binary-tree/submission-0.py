# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def levelOrderRec(root, level, levels):
            if root is None:
                return
            if len(levels) <= level:
                levels.append([])
            levels[level].append(root.val)
            levelOrderRec(root.left, level + 1, levels)
            levelOrderRec(root.right, level + 1, levels)
        level,levels=0,[]
        levelOrderRec(root,level,levels)
        return levels