# [BOJ] 1138. 한 줄로 서기(PyPy)
# 실행 시간 : 1676 ms
# 메모리 : 110592 KB

from itertools import permutations

N = int(input())
people = list(map(int, input().split()))

for p_case in permutations(range(1, N + 1), N):
    order_list = [0] * N
    for i in range(N):
        for j in range(i):
            if p_case[j] > p_case[i]:
                order_list[p_case[i] - 1] += 1
    
    for i in range(N):
        if people[i] != order_list[i]:
            break
    else:
        print(*p_case)
        break