# [Programmers] 12914. 멀리 뛰기

def solution(n):
    
    if n == 1:
        return 1
    
    memo = [1, 2]
    
    while len(memo) < n:
        memo.append((memo[-2] + memo[-1]) % 1234567)
        
    return memo[-1]