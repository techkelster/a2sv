class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        all_nums = set()
        for interval in ranges:
            all_nums.update(set(range(interval[0], interval[1] + 1)))
        for val in range(left, right + 1):
            if not (val in all_nums):
                return False
        return True
        