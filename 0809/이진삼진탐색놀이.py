import sys

def max_bin(N):
    if N == 1:
        return 0
    else:
        n = 1
        while True:
            if 2**(n+1) - 1 > N:
                return n
            n += 1

def max_tern(N):
    if N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        i = 2
        n = 1
        tmp = 2
        while True:
            tmp += 3**n
            if N <= tmp:
                return i
            n += i%2
            i += 1

Q = int(sys.stdin.readline().rstrip())
for i in range(Q):
    N = int(sys.stdin.readline().rstrip())  
    print(max_bin(N), max_tern(N))