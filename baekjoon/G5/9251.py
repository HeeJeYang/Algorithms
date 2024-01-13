# [BOJ] 9251. LCS
# 소요 시간 : 

word1 = input()
word2 = input()
cur_word = ""
# dp[n][0]은 해당 알파벳을 포함할 때의 최대 길이 부분 수열
# dp[n][1]은 해당 알파벳을 포함하지 않을 때의 최대 길이 부분 수열
dp = [[""] * 2 for _ in range(len(word1) + 1)]

for idx, c in enumerate(word1, start=1):
    word_idx = 0
    # while word_idx < len(word2):
    #     if word2[word_idx] == c:
    #         if len(dp[idx - 1][0]) + 1 < len(dp[idx - 1][1])