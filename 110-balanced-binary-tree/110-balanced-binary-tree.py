# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balanced(root)
       
    def height(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
        
    def balanced(self, root):
        if root == None:
            return True
        left = self.balanced(root.left)
        right = self.balanced(root.right)
        if left and right:
            lh = self.height(root.left)
            rh = self.height(root.right)
            if abs(lh - rh) <= 1:
                return True
        return False
            
        