class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_list2 = {}
        the_list = []
        for i in range(len(list2)):
            dict_list2[list2[i]] = i
        for i in range(len(list1)):
            if list1[i] in dict_list2:
                the_list.append([i + dict_list2[list1[i]], list1[i]])
        the_list.sort()
        ans = [the_list[0][1]]
        for i in range(1, len(the_list)):
            if the_list[i][0] == the_list[0][0]:
                ans.append(the_list[i][1])
        return ans
        