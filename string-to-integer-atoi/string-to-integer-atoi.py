class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        temp = []
        res = 0
        neg = 1
        if len(s) >= 1:            
            if s[0] == '-' or s[0] == '+':
                if len(s) == 1:
                    return 0
                if s[0] == '-':
                    neg = -1
                s = s[1:]
            for x in s:
                if x.isnumeric():
                    temp.append(x)
                else:
                    break
        exp = 0
        for x in range (len(temp) - 1, -1, -1):
            res += int(temp[x]) * (10 ** exp)
            exp += 1
        res *= neg
        if res < -2147483648:
            return -2147483648
        elif res > 2147483647:
            return 2147483647
        else:
            return res