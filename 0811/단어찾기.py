import sys

def horizontal(S, table, N, M):
    S_reverse = S[::-1]
    for i in range(N):
        for j in range(M-len(S)+1):
            start = j
            cnt = 0
            cnt_reverse = 0
            for s in range(len(S)):
                if table[i][j+s] == S[s]:
                    cnt += 1
                if table[i][j+s] == S_reverse[s]:
                    cnt_reverse += 1
            if cnt == len(S) or cnt_reverse == len(S):
                return True
    return False

def vertical(S, table, N, M):
    S_reverse = S[::-1]
    for i in range(M):
        for j in range(N-len(S)+1):
            start = j
            cnt = 0
            cnt_reverse = 0
            for s in range(len(S)):
                if table[j+s][i] == S[s]:
                    cnt += 1
                if table[j+s][i] == S_reverse[s]:
                    cnt_reverse += 1
            if cnt == len(S) or cnt_reverse == len(S):
                return True
    return False

def diagonal(S, table, N, M):

    S_reverse = S[::-1]
    table_reverse = [i[::-1] for i in table]

    for i in range(N-len(S)+1):
        for j in range(M-len(S)+1):
            start_x = i
            start_y = j
            cnt = 0
            cnt_reverse = 0
            for s in range(len(S)):
                if table[start_x+s][start_y+s] == S[s]:
                    cnt += 1
                if table[start_x+s][start_y+s] == S_reverse[s]:
                    cnt_reverse += 1
            if cnt == len(S) or cnt_reverse == len(S):
                return True
    
    for i in range(N-len(S)+1):
        for j in range(M-len(S)+1):
            start_x = i
            start_y = j
            cnt = 0
            cnt_reverse = 0
            for s in range(len(S)):
                if table_reverse[start_x+s][start_y+s] == S[s]:
                    cnt += 1
                if table_reverse[start_x+s][start_y+s] == S_reverse[s]:
                    cnt_reverse += 1
            if cnt == len(S) or cnt_reverse == len(S):
                return True
    
    return False

def find_S(S, table, N, M):
    S = list(S)
    len_S = len(S)
    if len_S <= N:
        if horizontal(S, table, N, M):
            print(1)
            return 
    if len_S <= M:
        if vertical(S, table, N, M):
            print(1)
            return
    if len_S <= N and len_S <= M:
        if diagonal(S, table, N, M):
            print(1)
            return

    print(0)


S = sys.stdin.readline().rstrip()
N, M = list(map(int, sys.stdin.readline().split()))
table = [list(sys.stdin.readline()) for _ in range(N)]

if len(S) > M and len(S) > N:
    print(0)
else:
    find_S(S, table, N, M)
