# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, len(nums), nums)
        
    def helper(self, i, j, nums):
        if not i < j:
            return None
        
        mid = (i + j) // 2
        root = TreeNode(nums[mid], None, None)
        root.left = self.helper(i, mid, nums)
        root.right = self.helper(mid + 1, j, nums)
        
        return root