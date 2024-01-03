class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = num < 0
        if neg:
            num = abs(num)
        filtered = []
        strnum = str(num)
        size = len(strnum)
        for i in str(num):
            if i != '0':
                filtered.append(i)

        if len(strnum) > 1:
            if not neg:
                strnum = sorted(filtered)
                strnum = ''.join(strnum[0]) + "0" * (size - len(filtered)) + "".join(strnum[1:])
            else:
                strnum = sorted(filtered, reverse=True)
                strnum = '-' + ''.join(strnum) + "0" * (size - len(filtered))
        return int(strnum)
        

        
        