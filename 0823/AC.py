import sys
from collections import deque

def AC(p, n, lst):
    direction = True
    p.replace("RR", "")
    if len(lst) < p.count('D'):
        return "error"
    for char in p:
        if char == 'R':
            direction = not direction
        elif char == 'D':
            if lst:
                if direction:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                return "error"
    if lst:
        if direction:
            return f"[{','.join(lst)}]"
        else:
            return f"[{','.join(reversed(lst))}]"
    return "[]"

    return
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline().rstrip()[1:-1].split(",")
    lst = deque(lst)
    if n == 0:
        lst = []
    print(AC(p, n, lst))
