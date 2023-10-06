class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        j = len(skill) - 1
        res = []
        flag = True
        for i in range(len(skill)//2):
            res.append((skill[i], skill[j]))
            j -= 1
        me = res[0][0] + res[0][1]
        sum_up = 0
        for k in res:
            if(me != k[0] + k[1]):
                flag =  False
                sum_up = -1
                break
            me = k[0] + k[1]
            sum_up += k[0] * k[1]
        return sum_up
                
                
            
            
            
            
            
        