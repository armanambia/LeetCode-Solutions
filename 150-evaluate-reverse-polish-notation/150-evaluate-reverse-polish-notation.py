class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            # print(x,stack)
            if x == "+":
                stack.append(stack.pop() + stack.pop())
            elif x == "-":
                sec = stack.pop()
                stack.append(stack.pop() - sec)
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
            elif x == "/":
                val1 = float(stack[-2])
                val2 = float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(val1 / val2))
            else:
                stack.append(int(x))
        return stack.pop()