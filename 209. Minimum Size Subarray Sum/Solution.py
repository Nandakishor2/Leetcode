class Solution(object):
    def minSubArrayLen(self, target, nums):
        minimum = float('inf')
        start = 0
        sumval = 0
        for end in range(len(nums)):
            sumval+=nums[end]
            while sumval >= target:
                sumval-=nums[start]
                minimum = min(minimum,end-start+1)
                start+=1
                
        return minimum if minimum != float('inf') else 0