class Solution:
    def intToRoman(self, num: int) -> str:
        # greedy alg
        dp = [''] * (num + 1)
        for x in range(1, num+1):
            if x >= 1000:
                dp[x] = 'M' + dp[x-1000]
            elif x >= 900:
                dp[x] = 'CM' + dp[x-900]
            elif x >= 500:
                dp[x] = 'D' + dp[x-500]
            elif x >= 400:
                dp[x] = 'CD' + dp[x-400]
            elif x >= 100:
                dp[x] = 'C' + dp[x-100]
            elif x >= 90:
                dp[x] = 'XC'+ dp[x-90]
            elif x >= 50:
                dp[x] = 'L' + dp[x-50]
            elif x >= 40:
                dp[x] = 'XL' + dp[x-40]
            elif x >= 10:
                dp[x] = 'X' + dp[x-10]
            elif x >= 9:
                dp[x] = 'IX' + dp[x-9]
            elif x >= 5:
                dp[x] = 'V' + dp[x-5]
            elif x >= 4:
                dp[x] = 'IV' + dp[x-4]
            elif x >= 1:
                dp[x] = 'I' + dp[x-1]
            
        
        return ''.join(dp[num])