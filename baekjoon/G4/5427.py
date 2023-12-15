# [BOJ] 5427. 불
# 실행 시간 : 00 ms
# 메모리 : 00 KB

from collections import deque
import sys
input = sys.stdin.readline

def fire():
    while fire_q:
        fy, fx = fire_q.popleft()

        for dy, dx in direction:
            ny, nx = fy + dy, fx + dx
            
            if 0 <= ny < h and 0 <= nx < w and building_map[ny][nx] == "." and fire_map[ny][nx] == 0:
                fire_map[ny][nx] = fire_map[fy][fx] + 1
                fire_q.append((ny, nx))


def bfs(sy, sx):
    bfs_q = deque()
    bfs_q.append((sy, sx))
    visited = [[0] * w for _ in range(h)]
    visited[sy][sx] = 1

    while bfs_q:
        y, x = bfs_q.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                return visited[y][x]

            if visited[ny][nx] == 0 and building_map[ny][nx] == "." and (fire_map[ny][nx] == 0 or fire_map[ny][nx] - 1 > visited[y][x]):
                visited[ny][nx] = visited[y][x] + 1
                bfs_q.append((ny, nx))

    return "IMPOSSIBLE"

T = int(input())
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(T):
    w, h = map(int, input().split())
    building_map = []
    fire_q = deque()
    fire_map = [[0] * w for _ in range(h)]
    sy, sx = -1, -1
    for i in range(h):
        row = list(input())
        for j in range(w):
            if row[j] == "*":
                fire_q.append((i, j))
                fire_map[i][j] = 1
            elif row[j] == "@":
                sy, sx = i, j
                row[j] = "."
        building_map.append(row)

    fire()
    print(bfs(sy, sx))