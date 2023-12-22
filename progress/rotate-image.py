class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vals = list(zip(*matrix))
        for i in range(len(vals)):
            matrix[i] = list(reversed(vals[i]))
    
            

        