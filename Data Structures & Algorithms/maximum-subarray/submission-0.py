class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        maxUntil = [0] * len(nums)
        maxUntil[0] = nums[0]
        for i in range(1, len(nums)): 
            cur = nums[i]
            if cur > maxUntil[i-1] + cur: 
                maxUntil[i] = cur
            else: 
                maxUntil[i] = cur + maxUntil[i-1]
        return max(maxUntil)

        

        