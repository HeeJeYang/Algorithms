# [BOJ] 18405. 경쟁적 전염
# 소요 시간 : 104 ms
# 메모리 : 34096 KB

from collections import deque
import sys
input = sys.stdin.readline


def bfs(queue):
    for _ in range(len(queue)):
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                board[ny][nx] = board[y][x]
                queue.append((ny, nx))


N, K = map(int, input().split())
board = []
board_info = dict()
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] != 0:
            if board_info.get(row[j]):
                board_info[row[j]].append((i, j))
            else:
                board_info[row[j]] = deque([(i, j)])
    board.append(row)

S, X, Y = map(int, input().split())
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(S):

    for virus in sorted(board_info.keys()):
        bfs(board_info[virus])

    if board[X - 1][Y - 1] != 0:
        break

print(board[X - 1][Y - 1])