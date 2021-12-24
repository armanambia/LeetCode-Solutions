class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchHelper(nums, 0, len(nums), target)
    def searchHelper (self, nums, start, end, target):
        mid = (end + start) // 2
        if end <= start:
            return start
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchHelper(nums, start, mid, target)
        else:
            return self.searchHelper(nums, mid+1, end, target)