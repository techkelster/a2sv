class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def removeDot(x):
            if x != ".":
                return int(x)
            else:
                return x
        def isNotP(x):
            return x != '.'

        bunchThree = [[], [], [], [], [], [], [], [], []]
        counter = 0
        mod = 2
        board_col = list(zip(*board))

        for i in range(len(board)):
            row = map(removeDot, board[i])
            col = map(removeDot, board_col[i])
           
            rc = list(row)
            bunchThree[counter].extend(rc[:3])
            bunchThree[counter + 1].extend(rc[3:6])
            bunchThree[counter + 2].extend(rc[6:])

            if i % mod == 0 and i != 0:
                mod += 3
                counter += 3

            listed = list(filter(isNotP, rc))
            if len(listed) != len(set(listed)):
                return False

            listed = list(filter(isNotP, list(col)))
            if len(listed) != len(set(listed)):
                return False 
        print(bunchThree)
        for i in bunchThree:
            i = list(filter(isNotP,map(removeDot, i)))
            if len(set(i)) != len(i):
                return False

        return True
            
        