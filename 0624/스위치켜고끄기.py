def toggle(switches, i):
    if switches[i] == 0:
        switches[i] = 1
    elif switches[i] == 1:
        switches[i] = 0

def toggle_switch(switches, student_type, num, num_switches):
    if student_type == 1:
        for i in range(num, num_switches+1, num):
            toggle(switches, i-1)
    elif student_type == 2:
        max_iter = min(num_switches-num, num-1)
        toggle_nums = [num-1]
        for i in range(1, max_iter+1):
            if switches[num-i-1] == switches[num+i-1]:
                toggle_nums.append(num-i-1)
                toggle_nums.append(num+i-1)
            else:
                break
        for toggle_num in toggle_nums:
            toggle(switches, toggle_num)

num_switches = int(input())
switches = list(map(int, input().split()))
num_students = int(input())

for _ in range(num_students):
    student_type, num = list(map(int, input().split()))
    toggle_switch(switches, student_type, num, num_switches)

for i in range(0, num_switches, 20):
    print(*switches[i:i+20])  
