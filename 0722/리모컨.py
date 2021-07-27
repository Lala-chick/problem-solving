import sys

def go_channel(N, break_buttons):
    if N == 100:
        return 0
    ans = abs(N - 100)
    for i in range(1000001):
        for num in str(i):
            if num in break_buttons:
                break
        else:
            ans = min(ans, abs(i-N)+len(str(i)))

    return ans

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
break_buttons = list(sys.stdin.readline().split())
print(go_channel(N, break_buttons))