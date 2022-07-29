class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i,v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            f = i + 1
            b = len(nums) - 1
            while f < b:
                target = [v, nums[f], nums[b]]
                total = sum(target)
                if  total < 0:
                    f += 1
                elif total > 0:
                    b -= 1
                else:
                    res.append(target)
                    f += 1
                    while f!= b and nums[f] == nums[f-1]:
                        f += 1
                    
        return res