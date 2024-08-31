class Solution(object):
    def longestConsecutive(self, nums):
        data = set(nums)
        maxlength = 0
        for dat in data:
            if dat-1 not in data:
                temp = dat
                count = 0
                while temp in data:
                    temp+=1
                    count+=1
                maxlength = max(maxlength,count)
                
        return maxlength