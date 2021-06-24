from collections import deque

def calc_scores(stack, mode):
    tmp_score = 0
    while stack:
        prev_bracket = stack.pop()
        if mode == 0:
            if prev_bracket == '(':
                if tmp_score == 0:
                    stack.append(2)
                else:
                    stack.append(2*tmp_score)
                break
            elif prev_bracket == '[':
                print(0)
                exit(0)
            else:
                tmp_score += prev_bracket
        if mode == 1:
            if prev_bracket == '[':
                if tmp_score == 0:
                    stack.append(3)
                else:
                    stack.append(3*tmp_score)
                break
            elif prev_bracket == '(':
                print(0)
                exit(0)
            else:
                tmp_score += prev_bracket
        

brackets = list(input())

stack = deque()
flag = False
for bracket in brackets:
    if bracket == ')':
        calc_scores(stack, 0)
    elif bracket == ']':
        calc_scores(stack, 1)
    else:
        stack.append(bracket)

if '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(stack))