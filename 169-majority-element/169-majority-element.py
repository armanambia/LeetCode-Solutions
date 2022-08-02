class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fmap = {}
        for x in nums:
            fmap[x] = fmap.get(x,0) + 1
            if fmap[x] > len(nums)/2:
                return x