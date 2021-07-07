import sys

H, W = list(map(int, sys.stdin.readline().split()))

blocks = list(map(int, sys.stdin.readline().split()))

max_height = max(blocks)
max_index = blocks.index(max_height)

block = 0

new_blocks_left = []

for i in range(max_index):
    if blocks[i] < block:
        new_blocks_left.append(block)
    elif blocks[i] >= block:
        block = blocks[i]
        new_blocks_left.append(block)
        
new_blocks_left.append(max_height)

block = 0
new_blocks_right = []

for i in range(W-1, max_index, -1):
    if blocks[i] < block:
        new_blocks_right.append(block)
    elif blocks[i] >= block:
        block = blocks[i]
        new_blocks_right.append(block)
        

answer = (sum(new_blocks_left) + sum(new_blocks_right)) - sum(blocks)
print(answer)
