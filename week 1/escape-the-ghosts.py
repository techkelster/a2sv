class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        your_steps = abs(target[0]) + abs(target[1])
        for i in range(len(ghosts)):
            ghost_steps = abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1])
            if your_steps >= ghost_steps:
                return False
        return True
        
        
        