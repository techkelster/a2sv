class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        digonals = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j in digonals:
                    digonals[i + j].append(mat[i][j])
                else:
                    digonals[i + j] = [mat[i][j]]
        # print(digonals)
        ans = []
        for digonal in digonals.items():
            if digonal[0] % 2 == 0:
                [ans.append(x) for x in digonal[1][::-1]]
            else:
                [ans.append(x) for x in digonal[1]]
        return ans 
        