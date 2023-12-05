class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_candy = max(candies)
        isgreatest_bool = [0] * len(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest_candy:
                isgreatest_bool[i] = True
            else:
                isgreatest_bool[i] = False
        return isgreatest_bool