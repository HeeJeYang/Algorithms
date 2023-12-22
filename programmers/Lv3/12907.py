# [Programmers] 12907. 거스름돈

def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for m in money:
        for i in range(1, len(dp)):
            if i >= m:
                dp[i] = (dp[i] + dp[i - m]) % 1000000007
    
    return dp[-1]