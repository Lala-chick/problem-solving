import sys

N = int(sys.stdin.readline().rstrip())

if N % 2 == 1:
    print("SK")
elif N % 2 == 0:
    print("CY")
