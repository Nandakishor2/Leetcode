class Solution:
    def findMaxLength(self, nums):
        nums = [-1 if i == 0 else 1 for i in nums]
        prefix = [0]*(len(nums)+1)
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1]+nums[i-1]
        data = {}
        maxlength = 0
        for i in range(len(prefix)):
            if prefix[i] in data:
                difference = i - data[prefix[i]]
                maxlength = max(maxlength,difference)

            else:
                data[prefix[i]] = i
        return maxlength