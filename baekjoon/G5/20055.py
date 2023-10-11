# [BOJ] 20055. 컨베이어 벨트 위의 로봇
# 소요 시간 : 60분

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque(list(map(int, input().split())))
robots = deque([0] * (2 * N))
robot_idx = 1
step = 0
zero_cnt = 0

while True:
    step += 1                           # 단계 증가
    
    # 1번
    queue.rotate(1)                     # 회전

    # 2번
    robots.rotate(1)
    robots[N - 1] = 0
    # for i in range(len(robots)):        # 각 로봇
    #     if robots[i] == 0: continue
    #     robots[i] += 1                  # 한 칸 전진
    #     if robots[i] == N - 1:          # 내리는 위치라면
    #         del robots[i]               # 해당 로봇 제외

    # 3번
    for i in range(len(robots) - 2, -1, -1):        # 각 로봇
        if robots[i] == 0: continue
        if queue[i + 1] != 0 and robots[i + 1] == 0:   # 한칸 앞의 내구도가 0이고, 로봇이 없으면
            robots[i], robots[i + 1] = 0, robots[i]              # 한 칸 전진
            queue[i + 1] -= 1       # 내구도 감소
            if queue[i + 1] == 0:
                zero_cnt += 1
            if i + 1 == N - 1:
                robots[i + 1] = 0
    if queue[0] != 0:
        robots[0] = robot_idx
        robot_idx += 1
        queue[0] -= 1
        if queue[0] == 0:
            zero_cnt += 1
    
    if zero_cnt >= K:
        break

print(step)