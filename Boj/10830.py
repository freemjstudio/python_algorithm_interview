# 10830 행렬 제곱 

N, b = map(int, input().split())
matrix = [list(map(int, input().split()) for _ in range(N))]

# 행렬 곱셈 함수 
def multiply():
    result = [[0]*n for _ in range(n)] 
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += matrix[row][i] * matrix[i][col]
            result[row][col] = e
    return result
