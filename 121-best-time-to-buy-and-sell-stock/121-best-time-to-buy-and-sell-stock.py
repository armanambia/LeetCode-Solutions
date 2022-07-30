class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        maxp = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                maxp = max(maxp, prices[r]-prices[l])
            r += 1
        return maxp
            