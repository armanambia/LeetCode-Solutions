import collections

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = collections.deque()
        max_len = 0
        for letter in s:
            if letter in q:
                while letter in q:
                    q.popleft()
            q.append(letter)
            if len(q) > max_len:
                max_len = len(q)
        return max_len