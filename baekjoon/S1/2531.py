# [BOJ] 2531. 회전 초밥
# 소요 시간 : 108 ms
# 메모리 : 34036 KB

import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(N)]
sushi_info = defaultdict(int)
max_sushi_type = 0

for i in range(k):
    sushi_info[sushis[i]] += 1
max_sushi_type = len(sushi_info.keys())

if not sushi_info.get(c):
    max_sushi_type += 1

for i in range(k, N + k):
    i = i % N
    sushi_info[sushis[i - k]] -= 1
    if sushi_info[sushis[i - k]] == 0:
        del sushi_info[sushis[i - k]]
    sushi_info[sushis[i]] += 1
    sushi_type = len(sushi_info.keys())
    if not sushi_info.get(c):
        sushi_type += 1
    max_sushi_type = max(max_sushi_type, sushi_type)

print(max_sushi_type)        

