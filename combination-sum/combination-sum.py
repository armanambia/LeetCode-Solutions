class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(nums, [], ret, target)
        return ret
    def dfs(self, nums, path, ret, target):
        if sum(path) > target or path in ret:
            return
        else:
            if sum(path) == target:
                ret.append(path)
            for i in range(len(nums)):
                self.dfs(nums[i:], path + [nums[i]], ret, target)
                self.dfs(nums[i+1:], path + [nums[i]], ret, target)