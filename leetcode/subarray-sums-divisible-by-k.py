class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        remainder_count = {0: 1}  
        for num in nums:
            running_sum += num
            remainder = running_sum % k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count