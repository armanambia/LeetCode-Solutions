class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        long_num = nums1 if len(nums1) > len(nums2) else nums2
        short_num = nums2 if long_num == nums1 else nums1 
        umap = {}
        for x in long_num:
            umap[x] = 1
        res = []
        for x in umap:
            if x in short_num:
                res.append(x)
        return res