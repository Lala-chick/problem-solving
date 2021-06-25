def rotating_queue(N, wanted):

    queue = [i+1 for i in range(N)]
    queue_reverse = [i+1 for i in range(N)]

    cnt = 0

    for number in wanted:
        if queue[0] == number:
            queue.pop(0)
            queue_reverse.pop(0)
            continue
        right = 0
        left = 0

        while True:
            queue = queue[1:] + [queue[0]]
            right += 1
            if queue[0] == number:
                queue.pop(0)
                break
        
        while True:
            queue_reverse = [queue_reverse[-1]] + queue_reverse[:-1]
            left += 1
            if queue_reverse[0] == number:
                queue_reverse.pop(0)
                break
        
        cnt += min(left, right)

    return cnt

N, M = list(map(int, input().split()))
wanted = list(map(int, input().split()))

answer = rotating_queue(N, wanted)
    
print(answer)