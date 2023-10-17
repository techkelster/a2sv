class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic_c = {}
        res = []
        for i in cpdomains:
            times_dom = i.split()
            dom_alone = times_dom[1].split(".")
            j = ''
            for i in range(len(dom_alone) - 1, -1 , -1):
                j = dom_alone[i] + j
                if j in dic_c:
                    dic_c[j] += int(times_dom[0])
                else:
                    dic_c[j] = int(times_dom[0])
                j = "." + j
        
        for key in dic_c:
            res.append(f"{dic_c[key]} {key}")
        return res
            