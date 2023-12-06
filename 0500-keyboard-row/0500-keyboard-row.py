class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        def checkRow(letter):
            first_row = "qwertyuiop"
            second_row = "asdfghjkl"
            if letter in first_row:
                return 1
            elif letter in second_row:
                return 2
            else:
                return 3
        for word in words:
            temp = word.lower()
            add = word
            for i in range(len(word) - 1):
                if checkRow(temp[i]) != checkRow(temp[i + 1]):
                    add = ""
                    break
            if add:
                ans.append(word)
        return ans
                
        