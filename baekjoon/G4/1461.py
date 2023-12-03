# [BOJ] 1461. 도서관
# 실행 시간 : 40 ms
# 메모리 : 31120 KB


def clean_up(pos1, pos2):
    global answer
    for i in range(0, len(pos1), M):
        answer += pos1[i] * 2
    for i in range(0, len(pos2), M):
        answer += pos2[i] * 2
    answer -= pos2[0]        


N, M = map(int, input().split())
positions = list(map(int, input().split()))
minus_pos = []
plus_pos = []
answer = 0

for pos in positions:
    if pos > 0:
        plus_pos.append(pos)
    else:
        minus_pos.append(-pos)

minus_pos.sort(reverse=True)
plus_pos.sort(reverse=True)

if not minus_pos or (plus_pos and minus_pos[0] < plus_pos[0]):
    clean_up(minus_pos, plus_pos)
else:
    clean_up(plus_pos, minus_pos)

print(answer)