class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if left == 0 and right == 0:
            ans.append(string)
            return
        if left != 0:
            self.dfs(left-1, right, ans, string + "(")
        if right != 0:
            self.dfs(left, right-1, ans, string + ")")
