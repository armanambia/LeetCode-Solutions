class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        parsed = {}
        for i,v in enumerate(nums):
            if parsed.has_key(target-v):
                return [i, parsed[target-v]]
            parsed[v] = i
        