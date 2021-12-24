# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # preorder - root, left, right
        # inorder - left, root, right
        
        self.pre_ind = 0
        self.in_map = {x:inorder.index(x) for x in preorder}
        
        def recurse(start, stop):
            if start > stop:
                return None
            
            v = preorder[self.pre_ind]
            self.pre_ind += 1
            root = TreeNode(v)
            root.left = recurse(start, self.in_map[v] - 1)
            root.right = recurse(self.in_map[v] + 1, stop)
            return root
        
        return recurse(0, len(preorder) -1)