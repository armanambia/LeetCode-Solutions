class Solution(object):
    def majorityElement(self, nums):
        freq_map = {}
        freq = 0
        val = 0
        for x in nums:
            freq_map[x] = freq_map.get(x, 0) + 1
            temp = freq_map[x]
            if temp > freq:
                freq = temp
                val = x
        return val