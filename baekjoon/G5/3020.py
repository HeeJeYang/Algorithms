# [BOJ] 3020. 개똥벌레
# 실행 시간 : 00 ms
# 메모리 : 00 KB

import sys
input = sys.stdin.readline

def count_obstacles(obs, idx):
    start, end = 0, N // 2 - 1

    while start <= end:
        mid = (start + end) // 2
        if obs[mid] <= idx:
            start = mid + 1
        else:
            end = mid - 1
    
    return N // 2 - (end + 1)



N, H = map(int, input().split())
up_obs, down_obs = [], []
answer = [N, 0]

for i in range(N):
    if i % 2:
        down_obs.append(int(input()))
    else:
        up_obs.append(int(input()))

up_obs.sort()
down_obs.sort()

for idx in range(1, H + 1):
    cnt_broken_walls = count_obstacles(up_obs, H - idx) + count_obstacles(down_obs, idx - 1)

    if cnt_broken_walls < answer[0]:
        answer = [cnt_broken_walls, 1]

    elif cnt_broken_walls == answer[0]:
        answer[1] += 1

print(*answer)