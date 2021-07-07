import sys

def convolution(kernel, elements):
    result = 0
    for i in range(2):
        for j in range(2):
            result += kernel[i][j] * elements[i][j]
    
    if result == 4:
        return True
    return False



def find_square(board, board_copy, n, m):
    
    kernel = [[1,1],[1,1]]
    answer = 0

    for i in range(n-1):
        for j in range(m-1):
            elements = [[board[i][j], board[i+1][j]], [board[i][j+1], board[i+1][j+1]]]
            if convolution(kernel, elements):
                board_copy[i+1][j+1] = min(board_copy[i][j], board_copy[i+1][j], board_copy[i][j+1])
                board_copy[i+1][j+1] += 1 
    

    for i in range(n):
        for j in range(m):
            answer = max(answer, board_copy[i][j])

    return answer ** 2


n,m = list(map(int, sys.stdin.readline().split()))

board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
board_copy = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        board_copy[i][j] = board[i][j]


print(find_square(board, board_copy, n, m))