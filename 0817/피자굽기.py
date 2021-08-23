import sys

def make_pizza(ovens, pizzas, D):
    depth = 0
    idx = 0

    for i in reversed(range(D)):
        if idx >= len(pizzas):
            return depth+1
            
        if ovens[i] >= pizzas[idx]:
            idx += 1
            depth = i
    return 0


D, N = list(map(int, sys.stdin.readline().split()))
ovens = list(map(int, sys.stdin.readline().split()))
pizzas = list(map(int, sys.stdin.readline().split()))



for i in range(1,D):
    ovens[i] = min(ovens[i], ovens[i-1])

print(make_pizza(ovens, pizzas, D))
