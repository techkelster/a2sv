class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        start = arr[0] - arr[1] # -
        flag = 0
        if start >= 0:
            return False
        for i in range(len(arr) - 1):
            if flag == 1 and arr[i] - arr[i + 1] < 0:
                return False
            if flag == 0 and arr[i] - arr[i + 1] > 0:
                flag += 1
            if arr[i] - arr[i + 1] == 0:
                return False
        if flag == 0:
            return False
        return True
        
        