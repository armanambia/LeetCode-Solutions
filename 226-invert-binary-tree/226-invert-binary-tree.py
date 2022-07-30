# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = root
        if not root:
            return None
        
        self.invertTreeHelper(root, root.left, root.right)
        
        return node
        
        
    def invertTreeHelper(self, root, left, right):
        root.left = right
        root.right = left
        leftRoot = root.left
        rightRoot = root.right
        if leftRoot:
            self.invertTreeHelper(leftRoot, leftRoot.left, leftRoot.right)
        if rightRoot:
            self.invertTreeHelper(rightRoot, rightRoot.left, rightRoot.right)