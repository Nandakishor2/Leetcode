class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i-1])
        nums = list(reversed(nums))
        for i in range(1,len(nums)):
            postfix.append(postfix[i-1]*nums[i-1])
        postfix = list(reversed(postfix))
        return [postfix[i]*prefix[i] for i in range(len(prefix))]
        