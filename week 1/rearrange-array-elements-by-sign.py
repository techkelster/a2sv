class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        ans=[]
        for i,j in zip(pos,neg):
            ans.append(i)
            ans.append(j)
        return ans