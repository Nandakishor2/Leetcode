class Solution(object):
    def twoSum(self, nums, target):
       data  ={}
       for i in range(len(nums)):
            if target-nums[i] in data:
                return [i,data[target-nums[i]]]
            else:
                data[nums[i]] = i
