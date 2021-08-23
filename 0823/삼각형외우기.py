import sys

angle_sum = 0
angle_lst = []
for _ in range(3):
    tmp = int(sys.stdin.readline().rstrip())
    angle_sum += tmp
    angle_lst.append(tmp)

if angle_sum != 180:
    print("Error")
elif angle_sum == 180:
    if angle_lst[0] == angle_lst[1] == angle_lst[2] == 60:
        print("Equilateral")
    elif angle_lst[0] == angle_lst[1] or angle_lst[0] == angle_lst[2] or angle_lst[1] == angle_lst[2]:
        print("Isosceles")
    elif angle_lst[0] != angle_lst[1] and angle_lst[0] != angle_lst[2] and angle_lst[1] != angle_lst[2]:
        print("Scalene")