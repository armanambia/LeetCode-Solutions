class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        return self.searchHelper(nums, 0, len(nums)-1, target)
    def searchHelper(self, nums, start, stop, target):
        if start > stop:
            return -1
        mid = (start + stop) // 2
        # print(start, stop, mid, nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.searchHelper(nums, mid+1, stop, target)
        else:
            return self.searchHelper(nums, start, mid-1, target)