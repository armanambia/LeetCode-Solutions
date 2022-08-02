class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        fmap = {}
        for x in s:
            fmap[x] = fmap.get(x,0) + 1
            
        single = False
        res = 0
        for key in fmap.keys():
            cur = fmap[key]
            if cur % 2 == 0:
                res += fmap[key]
            elif cur > 1:
                res += cur - 1
                single = True
            else:
                single = True
        if single:
            res += 1
        return res