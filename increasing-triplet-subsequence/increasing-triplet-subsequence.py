class Solution(object):
    def increasingTriplet(self, nums):
        res = [float('inf'), float('inf'), float('inf')]
        for x in nums:
            if x <= res[0]:
                res[0] = x
            elif x <= res[1]:
                res[1] = x
            elif x <= res[2]:
                res[2] = x
                return True
        return False