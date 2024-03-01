# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def travers(root):
            if not root:
                return
            travers(root.left)
            ans.append(root.val)
            travers(root.right)
        travers(root)

        print(ans, 'after traversal')

        res = []
        counted = Counter(ans)
        for i in counted:
            res.append((counted[i], i))
        res.sort(reverse=True)

        print(res, 'the sorted')
        ans = []
        if len(res) == 1:
            return [res[0][1]]

        for i in range(len(res) - 1):
            ans.append(res[i][1])
            if res[i][0] != res[i + 1][0]:
                return ans
        if res[-2][0] == res[-1][0]:
            ans.append(res[-1][1])
        return ans
                



            
        