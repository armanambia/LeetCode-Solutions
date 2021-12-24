import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        hmap = {}
        
        for x in nums:
            if x in hmap:
                hmap[x] += 1
            else:
                hmap[x] = 1
        print(hmap)
        
        return heapq.nlargest(k, hmap.keys(), key = hmap.get)
        
        