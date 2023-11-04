# [BOJ] 12851. 숨바꼭질 2
# 소요 시간 : 00 분 10:23 ~

from collections import deque


def bfs(N):
    queue = deque()
    queue.append((N, 0))
    visited = [[0, 0] for _ in range(100001)]
    visited[N][0] += 1 # [개수, 시간]

    while queue:
        pos, time = queue.popleft()

        if pos == K:
            return [time, visited[pos][0]]

        for cur_pos in [pos - 1, pos + 1, pos * 2]:
            if 0 <= cur_pos <= 100000:
                if visited[cur_pos][1] == time + 1:
                    visited[cur_pos][0] += visited[pos][0]
                elif visited[cur_pos][1] == 0:
                    visited[cur_pos][0] = visited[pos][0]
                    visited[cur_pos][1] = time + 1                
                    queue.append((cur_pos, time + 1))


N, K = map(int, input().split())

answer = bfs(N)
print(*answer, sep="\n")