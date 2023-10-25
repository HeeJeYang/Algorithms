# [BOJ] 2096. 내려가기
# 소요 시간 : 30 분

import sys
input = sys.stdin.readline

N = int(input())
max_dp, min_dp = [0] * 3, [0] * 3
for i in range(N):
    numbers = list(map(int, input().split()))
    max_dp[0], max_dp[1], max_dp[2] = max(max_dp[:2]) + numbers[0], max(max_dp) + numbers[1], max(max_dp[1:]) + numbers[2]
    min_dp[0], min_dp[1], min_dp[2] = min(min_dp[:2]) + numbers[0], min(min_dp) + numbers[1], min(min_dp[1:]) + numbers[2]

print(max(max_dp), min(min_dp))