class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic_con = {}
        result = []
        for i in paths:
            spread = i.split()
            for i in range(1, len(spread)):
                spread_2 = spread[i].split("(")
                if spread_2[1][:-1] in dic_con:
                    dic_con[spread_2[1][:-1]].append(spread[0] +  "/" + spread_2[0])
                else:
                    dic_con[spread_2[1][:-1]] = [spread[0] +  "/" + spread_2[0]]
        for key in dic_con:
            if len(dic_con[key]) >= 2:
                res = []
                for val in dic_con[key]:
                    res.append(val)
                result.append(res)
        return result
                
            
            
            
        