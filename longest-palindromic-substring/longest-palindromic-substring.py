class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur = ""
        
        if len(s) < 2:
            return s[0]
        elif len(s) == 2:
            return s[0] if s[0] != s[1] else s
        else:
            for i in range(len(s)):
                # can either start bab
                opt1 = self.palindromeHelper(s, i, i)
                # or baab
                opt2 = ""
                if i!= len(s) - 1 and s[i] == s[i+1]:
                    opt2 = self.palindromeHelper(s, i, i+1) 
                opt3 = opt1 if len(opt1) > len(opt2) else opt2
                if len(opt3)> len (cur):
                    cur = opt3
        return cur
    
     # returns the palindrome starting at left and right indices
    def palindromeHelper(self, s, left, right):
        substr = ""
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            substr = s[left: right + 1]
            left -= 1
            right += 1
        return substr
    
    