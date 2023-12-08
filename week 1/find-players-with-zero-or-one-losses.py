class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        match_dic = {}
        winners = []
        losers = []
        for i in matches:
            if i[0] in match_dic:
                match_dic[i[0]][0] += 1
            else:
                match_dic[i[0]] = [1, 0]
            if i[1] in match_dic:
                match_dic[i[1]][1] += 1
            else:
                match_dic[i[1]] = [0, 1]
        for key in match_dic:
            if match_dic[key][1] == 0:
                winners.append(key)
            if match_dic[key][1] == 1 :
                losers.append(key)
        return [sorted(winners), sorted(losers)]
        

        
        