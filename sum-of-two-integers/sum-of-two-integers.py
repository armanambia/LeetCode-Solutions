class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        num = pow(2,a) * pow(2,b)
        res = log(num, 2)
        return int(res)