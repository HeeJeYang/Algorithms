# [BOJ] 14719. 빗물
# 실행 시간 : 44 ms
# 메모리 : 31256 KB

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
water = 0

for i in range(1, W - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1:])

    min_block = min(left, right)

    if blocks[i] < min_block:
        water += min_block - blocks[i]

print(water)