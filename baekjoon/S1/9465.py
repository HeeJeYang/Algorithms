# [BOJ] 9465. 스티커(PyPy3)
# 실행 시간 : 420 ms
# 메모리 : 201936 KB

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    stickers = [[0, 0] for _ in range(n)]
    dp = [0, 0, 0]
    for i in range(2):
        for idx, score in enumerate(map(int, input().split())):
            stickers[idx][i] = score
    
    for i in range(n):
        dp[0], dp[1], dp[2] = max(dp), max(dp[0], dp[2]) + stickers[i][0], max(dp[0], dp[1]) + stickers[i][1]

    print(max(dp))