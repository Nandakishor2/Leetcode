class Solution:
    def checkSubarraySum(self, nums, k):
        prefixsum = [0]*(len(nums)+1)
        for i in range(1,len(prefixsum)):
            prefixsum[i] =prefixsum[i-1] + nums[i-1]
        data = {}
        for i in range(len(prefixsum)):
            if prefixsum[i]%k in data:
                if i - data[prefixsum[i]%k] >=2:
                    return True
            else:
                data[prefixsum[i]%k]= i
        return False