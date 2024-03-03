class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, group, diff):
            group.append(node.val) 
            
            if node.left is not None: 
                diff = dfs(node.left, group, diff)
            if node.right is not None: 
                diff = dfs(node.right, group, diff)

            if node.left is None and node.right is None:
                diff = max(diff, max(group) - min(group)) 
            
            group.pop() 
            return diff

        return dfs(root, [], 0)