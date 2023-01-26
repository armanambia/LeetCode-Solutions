class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if (current == nums[i]):
                counter += 1
            else:
                counter -= 1
                if (counter == 0):
                    counter = 1
                    current = nums[i]
        return current

