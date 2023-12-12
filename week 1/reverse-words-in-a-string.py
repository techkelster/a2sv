class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        temp = []
        for word in words:
            if word.strip():
                temp.append(word)
        return ' '.join(temp[::-1])
            


        