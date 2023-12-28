class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        # for i in range(size):
        #     indMax = i 
        #     for j in range(i + 1, size):
        #         if heights[j] > heights[indMax]:
        #             indMax = j
        #     heights[i], heights[indMax] = heights[indMax], heights[i]
        #     names[i], names[indMax] = names[indMax], names[i]
        # return names

        # for i in range(1, size):
        #     j = i
        #     while j >= 0 and heights[i] < heights[j]:
        #         j -= 1
        #     heights[i], heights[j]  = heights[i], heights

        storage = [0] * (max(heights) + 1)
        ans = []

        mapper = dict(zip(heights, names))

        for i in heights:
            storage[i] += 1
        for j in range(len(storage)):
            ans = [j] * storage[j] + ans
       
        return [mapper[i] for i in ans]
        


                    

        