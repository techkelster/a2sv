class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        size = len(changed)
        ans = []
        if size % 2:
            return []
        changed.sort()
        count = Counter(changed)
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                ans.append(num)
            elif num > 0 and count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                ans.append(num)
        return ans if len(ans) == size / 2 else []
            



        