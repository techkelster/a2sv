class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        k = 0
        ans = []
        operations = 0
        while k < len(boxes):
            i = k - 1
            j = k + 1
            while i >= 0:
                if int(boxes[i]) > 0:
                    operations += (k - i)
                i -= 1
            while j < len(boxes):
                if int(boxes[j]) > 0:
                    operations += (j - k)
                j += 1
            ans.append(operations)
            operations = 0
            k += 1
        return ans
        


        