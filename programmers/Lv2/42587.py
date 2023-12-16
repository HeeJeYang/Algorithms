# [Programmers] 42587. 프로세스

from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    cnt = 0
    sorted_priorities = sorted(priorities[:])
    while True:
        if queue[0] == sorted_priorities[-1]:
            cnt += 1
            if location == 0:
                break
            sorted_priorities.pop()
            queue.popleft()
        else:
            queue.append(queue.popleft())
        
        location = (location - 1) % len(queue)
            
    return cnt