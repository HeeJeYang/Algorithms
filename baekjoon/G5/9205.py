# [BOJ] 9205. 맥주 마시면서 걸어가기
# 소요 시간 : 00 분

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

def in_range(sy, sx, ey, ex):
    return abs(sy - ey) + abs(sx - ex) <= 1000


def dfs(y, x, cnt):
    global answer

    if answer == "happy":
        return
    
    if in_range(y, x, rf_y, rf_x):
        answer = "happy"
        return

    for idx, store in enumerate(stores):
        if visited[idx] > cnt and in_range(y, x, store[0], store[1]):
            visited[idx] = cnt
            dfs(store[0], store[1], cnt + 1)

t = int(input())
for tc in range(t):
    n = int(input())
    sg_y, sg_x = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    visited = [101] * n
    rf_y, rf_x = map(int, input().split())
    answer = "sad"

    dfs(sg_y, sg_x, 1)
    print(answer)