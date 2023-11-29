class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        refr = len(strs[0])
        
        for k in range(len(strs)):
            if len(strs[k]) < refr:
                refr = len(strs[k])
            
        for i in range(refr):
            last = ""
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return prefix
                last = strs[j][i]
            prefix += last

        return prefix
        
        
        