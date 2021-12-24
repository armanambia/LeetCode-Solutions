class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i= mid + 1
            else:
                j = mid 
        temp = nums[i:] + nums[0:i]
        print(temp)
        
        i = 0
        j = len(nums)
        while i < j:
            mid = (i + j) // 2
            if temp[mid] == target:
                return nums.index(temp[mid])
            elif temp[mid] < target:
                i = mid + 1
            else:
                j = mid
        
        return -1