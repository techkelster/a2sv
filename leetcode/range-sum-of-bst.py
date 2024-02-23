# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        theSum = []
        low = low
        high = high
        def travers(root):
            if not root:
                return
            travers(root.left)
            if root.val >= low and root.val <= high:
                theSum.append(root.val)
            travers(root.right)
        travers(root)
        return sum(theSum)
