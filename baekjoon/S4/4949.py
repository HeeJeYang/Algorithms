# 균형잡힌 세상

import sys
input = sys.stdin.readline

brackets = {")": "(", "]": "["}

while True:
    sentence = input().rstrip()
    stack = []

    if sentence == ".":
        break
    
    for c in sentence:
        if c == ")" or c == "]":
            if stack and stack[-1] == brackets[c]:
                stack.pop()
            else:
                print("no")
                break
        elif c == "(" or c == "[":
            stack.append(c)

    else:
        print("no" if stack else "yes")