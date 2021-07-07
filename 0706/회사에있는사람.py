import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
dic = defaultdict(int)

for _ in range(N):
    strings = sys.stdin.readline().rstrip().split()
    if strings[-1] == 'enter':
        dic[strings[0]] += 1
    else:
        del dic[strings[0]]

for name in sorted(dic, reverse=True):
    print(name)