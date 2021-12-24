class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        for i, v in enumerate(s):
            if hmap.get(v) == None:
                hmap[v] = 1
            else:
                hmap[v] += 1
        
        for i, v in enumerate(s):
            if hmap[v] == 1:
                return i
        return -1