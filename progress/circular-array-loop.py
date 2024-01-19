class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        
        if N < 2:
            return False
        
        slow = 0 
        
        fast = nums[0] % N 
        fast = (fast + nums[fast]) % N 
        count = 0
        
        while count < N:
            
            count += 1
            
            if slow == fast:
                l = 0 
                step = nums[slow]
                ptr = (nums[slow] + slow) % N  
                
                while ptr != slow:
                    
                    if nums[ptr] * step < 0:
                        break
                    
                    ptr = (ptr + nums[ptr]) % N
                    l += 1
                    
                if l > 0 and ptr == slow:
                    return True 
                
                else: 
                    slow = (slow + 1) % N 
                    fast = (slow + nums[slow]) % N 
                    fast = (fast + nums[fast]) % N  
              
            else:
                slow = (slow + nums[slow]) % N 
                fast = (fast + nums[fast]) % N 
                fast = (fast + nums[fast]) % N 
            
        return False 