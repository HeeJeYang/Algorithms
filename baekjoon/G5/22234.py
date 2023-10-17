# [BOJ] 22234. 가희와 은행
# 소요 시간 : 11:20

from collections import deque
import sys
input = sys.stdin.readline

N, T, W = map(int, input().split())
answer = []
waiting = deque()

for _ in range(N):
    waiting.append(list(map(int, input().split())))

M = int(input())
not_reservation = [list(map(int, input().split())) for _ in range(M)]

not_reservation.sort(key=lambda x: -x[2])

time = 0
while time < W:
    Px, tx = waiting.popleft()
    working_time = min(W - time, tx, T)
    time += working_time
    while not_reservation and time >= not_reservation[-1][2]:
        waiting.append(not_reservation.pop()[:2])

    for _ in range(working_time):
        answer.append(Px)

    if working_time != tx:
        waiting.append([Px, tx - T])

print(*answer, sep="\n")