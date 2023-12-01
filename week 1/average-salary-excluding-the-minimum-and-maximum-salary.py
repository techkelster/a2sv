class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        the_sum = 0
        for i in range(1, len(salary) - 1):
            the_sum += salary[i]
        return the_sum / (len(salary) - 2)
        