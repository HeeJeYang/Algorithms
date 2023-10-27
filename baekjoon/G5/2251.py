# [BOJ] 2251. 물통
# 소요 시간 : 00 분

from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0, limits[2]])
    visited = set()
    visited.add((0, 0, limits[2]))
    answer = set()
    fill_type = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]

    while queue:
        cups = queue.popleft()

        if cups[0] == 0:
            answer.add(cups[2])
        
        for g, t in fill_type:
            if cups[g] == 0 or cups[t] == limits[t]:
                continue
            
            tmp = 0
            if cups[g] + cups[t] <= limits[t]:
                tmp = cups[g]
            else:
                tmp = limits[t] - cups[t]

            cups[t] += tmp
            cups[g] -= tmp
            cups_tuple = tuple(cups)

            if cups_tuple not in visited:
                visited.add(cups_tuple)
                queue.append(cups[:])
            
            cups[g] += tmp
            cups[t] -= tmp
                

    print(*sorted(list(answer)))


limits = list(map(int, input().split()))
bfs()