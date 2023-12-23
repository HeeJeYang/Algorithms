# [BOJ] 2665. 미로만들기
# 실행 시간 : 112 ms
# 메모리 : 34204 KB

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited = [[n * n] * n for _ in range(n)]
    visited[0][0] = 0
    answer = n * n

    while queue:
        y, x, cnt = queue.popleft()

        if y == n - 1 and x == n - 1:
            answer = min(answer, cnt)
            continue

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] > cnt:
                if maze[ny][nx] == "1":
                    visited[ny][nx] = cnt
                    queue.append((ny, nx, cnt))
                else:
                    visited[ny][nx] = cnt + 1
                    queue.append((ny, nx, cnt + 1))
        
    return answer


n = int(input())
maze = [input() for _ in range(n)]
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(bfs())