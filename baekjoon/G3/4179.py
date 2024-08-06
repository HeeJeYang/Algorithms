# 불!

import sys
from collections import deque
input = sys.stdin.readline


def bfs(queue):
    q = deque(queue)
    time = 0
    while q:

        time += 1
        for _ in range(len(q)):    
            y, x = q.popleft()

            if maze[y][x] == "J" and (y == 0 or y == R - 1 or x == 0 or x == C - 1):
                return visited[y][x]
        
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                
                if 0 <= ny < R and 0 <= nx < C:
                    if maze[y][x] == "F":
                        if maze[ny][nx] == "." or (maze[ny][nx] == "J" and visited[ny][nx] < time):
                            maze[ny][nx] = "F"
                            q.append((ny, nx))
                    else:
                        if maze[ny][nx] == ".":
                            maze[ny][nx] = "J"
                            visited[ny][nx] = visited[y][x] + 1
                            q.append((ny, nx))

    return "IMPOSSIBLE"


R, C = map(int, input().split())
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited = [[0] * C for _ in range(R)]
maze = []

jihun_y, jihun_x = -1, -1
fire_list = []

# -1: 벽, 0: 빈 공간, -2: 불
for y in range(R):
    row = list(input().rstrip())
    for x in range(C):
        if row[x] == "J":
            jihun_y, jihun_x = y, x
            visited[y][x] = 1
        elif row[x] == "F":
            fire_list.append((y, x))

    maze.append(row)

print(bfs(fire_list + [(jihun_y, jihun_x)]))