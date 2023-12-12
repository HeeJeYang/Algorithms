# [BOJ] 14500. 테트로미노
# 실행 시간 : 760 ms
# 메모리 : 38140 KB

import sys
input = sys.stdin.readline


def calculate(arr):
    R = len(arr)
    C = len(arr[0])
    max_sum = 0

    # ---- 의 경우
    for i in range(R):
        for j in range(C - 3):
                max_sum = max(
                    max_sum,
                    sum(arr[i][j:j + 4]),
                )

    # 나머지 경우
    for i in range(R - 1):
        for j in range(C - 2):
            arr1 = arr[i][j:j + 3]
            arr2 = arr[i + 1][j:j + 3]
            total = sum(arr1) + sum(arr2)
            max_sum = max(
                max_sum,
                total - min(
                    arr1[0] + arr1[1],
                    arr1[0] + arr1[2],
                    arr1[0] + arr2[0],
                    arr1[0] + arr2[2],
                    arr1[1] + arr1[2],
                    arr1[2] + arr2[0],
                    arr1[2] + arr2[2],
                    arr2[0] + arr2[1],
                    arr2[0] + arr2[2],
                    arr2[1] + arr2[2],
                )
            )

    return max_sum
    

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

rotated_paper = []
for j in range(M):
    row = []
    for i in range(N):
        row.append(paper[i][j])
    rotated_paper.append(row)

print(max(calculate(paper), calculate(rotated_paper)))