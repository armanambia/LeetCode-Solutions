class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''.join(c for c in s if c.isalnum())
        res = res.lower()
        print(res)
        return res == res[::-1]