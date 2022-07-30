class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''.join(c for c in s if c.isalnum())
        res = res.lower()
        f = 0
        b = len(res) - 1
        while f < b:
            if res[f] != res[b]:
                return False
            f += 1
            b -= 1
        if b == f:
            return res[b] == res[f]
        else:
            return True
            