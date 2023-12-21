class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(image)):
            ans.append(map(lambda x: 1 if x == 0 else 0, list(reversed(image[i]))))
        return ans
