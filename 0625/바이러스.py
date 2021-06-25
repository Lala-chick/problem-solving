from collections import defaultdict, deque
import sys


def virus(network, num_computers):
    visited = [0 for _ in range(num_computers)]
    queue = deque()
    queue.append(1)

    while queue:
        start_computer = queue.popleft()
        visited[start_computer - 1] = 1
        for computer in network[start_computer]:
            if visited[computer - 1] == 0:
                queue.append(computer)

    return visited


num_computers = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
network = defaultdict(list)

for _ in range(N):
    com1, com2 = list(map(int, sys.stdin.readline().rstrip().split()))
    network[com1].append(com2)
    network[com2].append(com1)


visited = virus(network, num_computers)
answer = sum(visited) - 1
print(answer)
