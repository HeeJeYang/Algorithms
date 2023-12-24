# [BOJ] 18188. 다오의 데이트
# 소요 시간 : 00 분

from collections import deque
import sys
input = sys.stdin.readline

def bfs(sy, sx, cnt, cmds):
    queue = deque()
    queue.append((sy, sx, cnt))
    visited = [[0] * W for _ in range(H)]
    visited[sy][sx] = 1
    
    while queue:
        y, x = queue.popleft()
        
    targets = ["W", "A", "S", "D"]
    if cnt <= len(marids):
        targets = marids[cnt]
    
    for target in targets:
        ny, nx = y + direction[target][0], x + direction[target][1]
        # if 0 <= ny < H and 0 <= nx < W and (ny, nx, )

direction = {
    "W": (-1, 0),
    "A": (0, -1),
    "S": (1, 0),
    "D": (0, 1),
}


H, W = map(int, input().split())
bubblehill = []
dao = [-1, -1]
for i in range(H):
    row = input()
    for j in range(W):
        if row[j] == "D":
            dao[0], dao[1] = i, j
    
    bubblehill.append(row)

N = int(input())
marids = [list(map(int, input().split())) for _ in range(N)]

answer = ""
bfs(dao[0], dao[1], 0, "")