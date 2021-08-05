import sys
from collections import defaultdict

def count_leaf(dic):
    answer = 0
    if -1 in dic:
        queue = [-1]
    else:
        queue = []
    while queue:
        node = queue.pop()
        if node not in dic:
            answer += 1
        else:
            queue += dic[node]
    return answer


N = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline().rstrip())
dic = defaultdict(list)

for idx, node in enumerate(lst):
    if node == delete or idx == delete:
        continue
    dic[node].append(idx)

print(count_leaf(dic))