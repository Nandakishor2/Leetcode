class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        data = {}
        for i in range(len(nums)):
            if nums[i] in data:
                if abs(data[nums[i]] - i) <= k :
                    return True
                else:
                    data[nums[i]] = i
            else:
                data[nums[i]] = i
        return False