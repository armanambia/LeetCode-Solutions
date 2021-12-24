class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        else:
            nums = sorted(nums)
            t_dist = float(inf)
            t_closest = 0
            for x in range(len(nums) - 2):
                cur =  nums[x]
                l = x + 1
                r = len(nums) -1
                while l < r:
                    temp = cur + nums[l] + nums[r]
                    if temp > target:
                        r -= 1
                    elif temp < target:
                        l += 1
                    else:
                        return temp
                    if abs(target - temp) < t_dist:
                        t_dist = abs(target-temp)
                        t_closest = temp
            return t_closest