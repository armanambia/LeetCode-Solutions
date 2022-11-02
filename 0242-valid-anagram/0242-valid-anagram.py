class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash_map = {}
        for x in s:
            hash_map[x] = hash_map.get(x, 0) + 1
        for x in t:
            hash_map[x] = hash_map.get(x, 0) - 1
            if x not in hash_map or hash_map[x] < 0:
                return False
        return True
