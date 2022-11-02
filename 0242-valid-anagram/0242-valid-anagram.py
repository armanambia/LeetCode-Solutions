class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash_map1 = {}
        for x in s:
            hash_map1[x] = hash_map1.get(x, 0) + 1
        for x in t:
            hash_map1[x] = hash_map1.get(x, 0) - 1
            if hash_map1[x] == None or hash_map1[x] < 0:
                return False
        return True
