class Solution(object):
    def twoSum(self, nums, target):
        prev = {}
        for i, val in enumerate(nums):
            seek = target - val
            if prev.get(seek) != None:
                return [prev[seek], i]
            prev[val] = i
        