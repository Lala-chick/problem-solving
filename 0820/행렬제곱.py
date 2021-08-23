import sys

def matmul(matrix_A, matrix_B):
    result = [[0]*len(matrix_A) for _ in range(len(matrix_B))]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B)):
            for k in range(len(matrix_A[0])):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
                result[i][j] %= 1000
    return result


N, B = list(map(int, sys.stdin.readline().split()))

mat = []
for _ in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))

answer = []
for j in range(N):
    answer.append([1 if i==j else 0 for i in range(N)])


while B != 1:
    tmp = mat[:]
    if B % 2 == 1:
        answer = matmul(answer, tmp)
        B -= 1
    else:
        mat = matmul(tmp, tmp)
        B //= 2

answer = matmul(answer, mat)
for ans in answer:
    print(*ans)
