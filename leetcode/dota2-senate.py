class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        size = len(senate)

        radiants = [i for i in range(len(senate)) if senate[i]=='R']
        dires = [j for j in range(len(senate)) if senate[j]=='D']
        
        while  radiants and dires:
            r = radiants.pop(0)
            d = dires.pop(0)
            if r < d:
                radiants.append(size + r)
            else:
                dires.append(size + d)
                
        return 'Radiant' if radiants else 'Dire'