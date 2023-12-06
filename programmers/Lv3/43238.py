# [Programmers] 43238. 입국심사

def solution(n, times):
    answer = 0
    long_time = max(times)
    start = 1
    end = long_time * n
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        print(start, end, mid)
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer