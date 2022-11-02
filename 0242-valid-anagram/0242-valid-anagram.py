class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map1 = {}
        for x in s:
            hash_map1[x] = hash_map1.get(x, 0) + 1
        for x in t:
            hash_map1[x] = hash_map1.get(x, 0) - 1
            if hash_map1[x] < 0:
                return False
        for value in hash_map1.values():
            if value: 
                return False
        return True
