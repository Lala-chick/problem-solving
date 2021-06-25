from collections import defaultdict, deque

def find_parent(tree, N):
    visited = [0 for _ in range(N)]
    queue = deque()
    queue.append(1)
    answer = [0 for _ in range(N)]

    while queue:
        parent = queue.popleft()
        visited[parent-1] = 1
        for child in tree[parent]:
            if visited[child-1] == 0:
                queue.append(child)
                answer[child-1] = parent

    return answer

N = int(input())
tree = defaultdict(list)

for _ in range(N-1):
    node1, node2 = list(map(int, input().split()))
    tree[node1].append(node2)
    tree[node2].append(node1)

answers = find_parent(tree, N)

for answer in answers[1:]:
    print(answer)