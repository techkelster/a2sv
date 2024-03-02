# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        queue =  deque([root])

        leftRight = True

        while queue:
            curVals = []
            
            for _ in range(len(queue)):
                node = queue.popleft()

                curVals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if leftRight:
                res.append(curVals)
            else:
                res.append(curVals[::-1])
            
            leftRight = not leftRight
        return res

                

