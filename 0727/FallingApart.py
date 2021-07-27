import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

alice = 0
bob = 0

for i in range(N):
    if i%2 == 0:
        alice += numbers.pop()
    else:
        bob += numbers.pop()

print(alice, bob)