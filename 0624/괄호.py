from collections import deque

def is_VPS(brackets):
    if brackets[-1] == '(':
        return "NO"

    queue = deque()

    for bracket in brackets:
        if bracket == '(':
            queue.append(bracket)
        elif bracket == ')':
            try:
                queue.pop()
            except:
                return "NO"
    if queue:
        return "NO"
    return "YES"


T = int(input())
answers = []
for _ in range(T):
    brackets = list(input())
    answers.append(is_VPS(brackets))

for answer in answers:
    print(answer)