class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        i = 4
        f = 2
        s = 3

        # Find & Displaying
        
        while(i <= n):
            f, s = s, f+s
            i += 1
        
        return s