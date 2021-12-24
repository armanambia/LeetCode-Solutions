# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        currentLevel = [root]
        if root == None:
            return ret
        while currentLevel:
            cur = []
            nxt = []
            for node in currentLevel:
                cur.append(node.val) 
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            ret.append(cur)
            currentLevel = nxt
        return ret