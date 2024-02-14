class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = sorted(costs, key = lambda x: x[0] - x[1])
        ans = 0
        for i in range(len(a)):
            if i < (len(a) // 2):
                ans += a[i][0]
            else:
                ans += a[i][1]
        return ans
            

        
        