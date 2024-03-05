# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, num_sum):
            if not node:
                return 0

            num_sum = num_sum * 10 + node.val
            if not node.left and not node.right:
                return num_sum
            return dfs(node.left, num_sum) + dfs(node.right, num_sum)
        return dfs(root, 0)

        