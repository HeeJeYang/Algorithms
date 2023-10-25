# [BOJ] 2805. 나무 자르기
# 소요 시간 : 00 분

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    target = sum([tree - mid if tree > mid else 0 for tree in trees])
    if target < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)