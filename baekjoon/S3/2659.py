# [BOJ] 2659. 십자카드 문제
# 실행 시간 : 00 ms
# 메모리 : 00 KB

from collections import deque

target = "".join(input().split())
t_set = set()
for _ in range(4):
    target = target[-1] + target[:3]
    t_set.add(int(target))

visited = set()
answer = 0
for num in range(1111, 10000):
    if num in visited: continue
    str_num = str(num)
    num_list = []
    for _ in range(4):
        str_num = str_num[-1] + str_num[:3]
        num_list.append(int(str_num))
        visited.add(int(str_num))
    if min(num_list) == num:
        answer += 1
        if num in t_set:
            print(answer)
            break

# for _ in range(4):
#     number = 0
#     for i in range(4):
#         number += numbers[i] * (10 ** (3 - i))
#     min_number = min(min_number, number)

#     numbers.rotate()

# answer = 0
# for i in range(4):
#     tmp = min_number % 10
#     answer += (tmp - 1) * (9 ** i)
#     min_number //= 10

# print(answer)