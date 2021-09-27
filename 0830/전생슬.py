import sys
import math

K = int(sys.stdin.readline().rstrip())
answer = 0
for i in range(2, K+1):
    while K > 0 and K%i ==0:
        K = K//i
        answer +=  1
    
if answer == 0:
    print(0)
else:
    print(int(math.ceil(math.log2(answer))))