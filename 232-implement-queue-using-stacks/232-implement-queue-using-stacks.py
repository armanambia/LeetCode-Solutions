class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        value = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return value

    def peek(self):
        """
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        value = self.s2[len(self.s2)-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return value

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()