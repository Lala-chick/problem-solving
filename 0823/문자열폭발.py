import sys

string = list(sys.stdin.readline().rstrip())
explode = list(sys.stdin.readline().rstrip())
length = len(explode)
stack = []

for char in string:
    stack.append(char)
    if len(stack) >= length:
        if stack[-1] == explode[-1]:
            if stack[-length:] == explode:
                del stack[-length:]
    
answer = ''.join(stack)

if answer:
    print(answer)
else:
    print("FRULA")