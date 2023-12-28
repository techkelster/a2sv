class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        middle = len(mat) // 2
        backward = 0
        forward = len(mat) - 1
        theSum = 0

        for i in range(forward + 1):
            for j in range(forward + 1):
                if i + j == forward or i - j == backward:
                    theSum += mat[i][j]
        return theSum
            


        