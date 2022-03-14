# 10830 행렬 제곱 

N, b = map(int, input().split())
matrix = [list(map(int, input().split()) for _ in range(N))]

# 행렬 곱셈 함수 
def multiply(matrix1,matrix2):
    n = len(matrix1)
    result = [[0]*n for _ in range(n)] 
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += matrix1[row][i] * matrix2[i][col]
            result[row][col] = e%1000
    return result

def square(B, M):
    if B == 1:
        for i in range(N):
            for j in range(N):
                M[i][j] %= 1000
        return M 
    