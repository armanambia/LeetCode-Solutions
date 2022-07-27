class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        nums = sorted(nums)
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s = i+1
            e = len(nums) - 1
            while s < e:
                total = v + nums[s] + nums[e]
                if total < 0:
                    s += 1
                elif total > 0:
                    e -= 1
                else:
                    res.append([v,nums[s],nums[e]])
                    s += 1
                    while nums[s] == nums[s-1] and s < e:
                        s += 1
        return res
                