nums = list(map(int, input().split()))

answer = sorted(nums)
while nums != answer:
    for  i in range(4):
        if nums[i] > nums[i+1]:
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
            print(*nums)
