# [BOJ] 2011. 암호코드
# 실행 시간 : 44 ms
# 메모리 : 31120 KB

code = input()
dp = [1, 1]

if code[0] == "0":
    print(0)
else:
    for i in range(len(code) - 1):
        # 두 자리 수 저장
        num = int(code[i:i + 2])

        # 암호가 잘못된 경우(00이거나 30, 40, ... 90 인 경우)
        if num == 0 or (num % 10 == 0 and num // 10 > 2):
            dp[1] = 0
            break

        # num이 10 미만인 경우 
        elif num < 10:
            dp[0] = dp[1]
        elif num == 10 or num == 20:
            dp[1] = dp[0]
        elif 10 <= num <= 26:
            dp[0], dp[1] = dp[1], (dp[0] + dp[1]) % 1000000
        else:
            dp[0] = dp[1]

    print(dp[1])