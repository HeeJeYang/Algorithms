# [BOJ] 1261. 알고스팟
# 실행 시간 : 68 ms
# 메모리 : 34088 KB

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and cnt_broken_walls_list[ny][nx] == -1:
                if maze[ny][nx] == "0":
                    cnt_broken_walls_list[ny][nx] = cnt_broken_walls_list[y][x]
                    queue.appendleft((ny, nx))
                else:
                    cnt_broken_walls_list[ny][nx] = cnt_broken_walls_list[y][x] + 1
                    queue.append((ny, nx))

    return cnt_broken_walls_list[-1][-1]


M, N = map(int, input().split())
maze = [input() for _ in range(N)]
cnt_broken_walls_list = [[-1] * M for _ in range(N)]
cnt_broken_walls_list[0][0] = 0

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(bfs())