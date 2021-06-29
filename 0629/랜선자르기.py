import sys

def cut_lan(N, lengths):
    start, end = 1, max(lengths)

    while start <= end:
        mid = (start + end) // 2
        num_lines = 0
        for length in lengths:
            num_lines += length // mid
        
        if num_lines >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

K, N = list(map(int, sys.stdin.readline().rstrip().split()))
lengths = [int(sys.stdin.readline()) for _ in range(K)]

print(cut_lan(N, lengths))
