class Solution(object):
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        avg = float(total) / k
        
        for i in range(1, len(nums) - k + 1):
            total -= nums[i - 1]
            total += nums[i + k - 1]
            avg = max(avg, float(total) / k)
        
        return avg
