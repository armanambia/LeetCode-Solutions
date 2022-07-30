class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,1
        maxSum = nums[0]
        prevSum = nums[0]
        while r < len(nums):
            if prevSum < 0:
                l = r
                prevSum = nums[r]
            else:
                prevSum += nums[r]
            
            maxSum = max(maxSum, prevSum)
            r += 1
        return maxSum
            