class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        x = abs(x)        
        exp = 0
        # map power to value and
        temp = {}
        while x > 0:
            temp[exp] = x % 10
            exp += 1
            x = x // 10
        max_exp = exp
        exp = 0
        res = 0
        while temp.get(exp) != None:
            res += temp[max_exp - exp - 1] * (10 ** exp)
            exp += 1
        res *= neg
        return 0 if res <= -2147483648 or res >= 2147483647 else res