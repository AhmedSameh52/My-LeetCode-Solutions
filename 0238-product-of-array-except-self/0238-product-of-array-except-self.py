class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(1, len(nums), 1):
            prefix = prefix * nums[i-1]
            outputArr[i] = prefix
        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            postfix = postfix * nums[i]
            outputArr[i-1] = outputArr[i-1] * postfix
        return outputArr