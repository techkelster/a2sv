# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def travers(root1, root2):
            if root1 and root2:
                if root1.val != root2.val:
                    return False
                return travers(root1.left, root2.right) and travers(root1.right, root2.left)
            return not root1 and not root2

        # if not root:
        #     return True

        return travers(root.left, root.right)
