class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        the_number = len(arr) * 0.25
        m = 1
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                m += 1
            elif m > the_number:
                return arr[i]
            else:
                m = 1
        return arr[-1] if m > the_number else arr[0]

        