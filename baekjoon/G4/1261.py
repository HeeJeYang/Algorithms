# [BOJ] 1261. 알고스팟
# 실행 시간 : 480 ms
# 메모리 : 34096 KB

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    min_cnt_broken_walls = 10000

    while queue:
        y, x, cnt_broken_walls = queue.popleft()
        
        if cnt_broken_walls >= min_cnt_broken_walls:
            continue

        if y == N - 1 and x == M - 1:
            min_cnt_broken_walls = min(min_cnt_broken_walls, cnt_broken_walls)
            continue

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == "0" and cnt_broken_walls_list[ny][nx] > cnt_broken_walls:
                    cnt_broken_walls_list[ny][nx] = cnt_broken_walls
                    queue.append((ny, nx, cnt_broken_walls))
                elif maze[ny][nx] == "1" and cnt_broken_walls_list[ny][nx] > cnt_broken_walls + 1:
                    cnt_broken_walls_list[ny][nx] = cnt_broken_walls + 1
                    queue.append((ny, nx, cnt_broken_walls + 1))

    return min_cnt_broken_walls


M, N = map(int, input().split())
maze = [input() for _ in range(N)]
cnt_broken_walls_list = [[10000] * M for _ in range(N)]
cnt_broken_walls_list[0][0] = 0

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(bfs())