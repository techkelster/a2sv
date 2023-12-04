from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderRef = {letter: value for value, letter in enumerate(order)}

        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]
            is_out_of_order = False

            for j in range(min(len(word_1), len(word_2))):
                if word_1[j] != word_2[j]:
                    if orderRef[word_2[j]] < orderRef[word_1[j]]:
                        return False
                    is_out_of_order = True
                    break
            
            if not is_out_of_order and len(word_1) > len(word_2):
                return False

        return True
