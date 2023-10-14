# [BOJ] 1063. 킹
# 소요 시간 : 18분

king_pos, stone_pos, N = input().split()
N = int(N)
king = [8 - int(king_pos[1]), ord(king_pos[0]) - 65]
stone = [8 - int(stone_pos[1]), ord(stone_pos[0]) - 65]

direction = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1),
}

for _ in range(N):
    command = input()
    d_king = [king[0] + direction[command][0], king[1] + direction[command][1]]
    if 0 <= d_king[0] < 8 and 0 <= d_king[1] < 8:
        if stone[0] == d_king[0] and stone[1] == d_king[1]:
                d_stone = [stone[0] + direction[command][0], stone[1] + direction[command][1]]
                if 0 <= d_stone[0] < 8 and 0 <= d_stone[1] < 8:
                    stone[0], stone[1] = d_stone[0], d_stone[1]
                else:
                    continue
        
        king[0], king[1] = d_king[0], d_king[1]
    else:
        continue

print(chr(king[1] + 65) + str(8 - king[0]))
print(chr(stone[1] + 65) + str(8 - stone[0]))