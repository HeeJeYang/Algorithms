# [BOJ] 15989. 1, 2, 3 더하기 4
# 실행 시간 : 60 ms
# 메모리 : 31252 KB

T = int(input())
tc_list = [int(input()) for _ in range(T)]
max_tc = max(tc_list)
dp = [[1] * (max_tc + 1) for _ in range(3)]

if max_tc > 1:
    dp[2][2] = 2

for i in range(2, max_tc + 1):
    dp[1][i] = dp[1][i - 2] + dp[0][i]

for i in range(3, max_tc + 1):
    dp[2][i] = dp[2][i - 3] + dp[1][i]

answer = []
for tc in tc_list:
    answer.append(dp[2][tc])

print(*answer, sep="\n")