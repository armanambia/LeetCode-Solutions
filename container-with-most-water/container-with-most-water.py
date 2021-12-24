class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, low, high = 0, 0, len(height) -1
        while low < high:
            result = max(result, min(height[low], height[high]) * (high - low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return result