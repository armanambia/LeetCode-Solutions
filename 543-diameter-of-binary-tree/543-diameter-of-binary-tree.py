# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max_len = 0
        self.diameter(root)
        return self.max_len
        
        
    def diameter(self,root):
        if root:
            self.max_len = max(self.max_len, self.height(root.left) + self.height(root.right))
            self.diameter(root.left)
            self.diameter(root.right)
        
        
    def height(self,root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
        
        