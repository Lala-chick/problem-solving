N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

cnt = 1
end_time = sorted_meetings[0][1]
for start, end in sorted_meetings[1:]:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)
