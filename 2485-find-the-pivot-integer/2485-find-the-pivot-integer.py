class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = 0
        left = 0
        for i in range(1, n + 1):
            total_sum += i
        right = total_sum 
        for i in range(1, n + 1):
            left += i
            if left == right:
                return i
            right -= i
        return -1
        
        
        
        
        
        
        
        
        
        
        