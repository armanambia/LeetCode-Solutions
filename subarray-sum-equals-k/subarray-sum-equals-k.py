class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        umap = {0:1}
        cumv = 0
        count = 0
        for x in range(len(nums)):
            cumv += nums[x]
            if (cumv - k) in umap:
                count += umap[cumv-k]
            if cumv not in umap:
                umap[cumv] = 0
            umap[cumv] += 1
        return count
            