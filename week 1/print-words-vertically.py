class Solution:
    def printVertically(self, s: str) -> List[str]:
        words_list = s.split()
        max_length = 0
        for i in words_list:
            if len(i)>max_length: max_length= len(i)
        vertical_words = {}
        for i in words_list:
            for j in range(max_length):
                try:
                    if j not in vertical_words:
                        vertical_words[j] = i[j]
                    else:
                        vertical_words[j]+=i[j]
                except:
                    if j not in vertical_words:
                        vertical_words[j] = " "
                    else:
                        vertical_words[j]+=" "
                    

        ans = []
        for i in vertical_words:
            ans.append(vertical_words[i].rstrip())
        return ans