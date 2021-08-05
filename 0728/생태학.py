import sys
from collections import defaultdict

dic = defaultdict(int)
cnt = 0

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    dic[tree] += 1
    cnt += 1

dic = sorted(dic.items(), key=lambda x:x[0])
for tree, num in dic:
    print(f"{tree} {num*100/cnt:.4f}")
