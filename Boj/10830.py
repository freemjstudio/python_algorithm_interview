# 10830 행렬 제곱 

from re import A


N, B = map(int, input().split())
array = []
result = []
for _ in range(N):
    array.append(list(map(int, input().split())))

# 홀수 , 짝수 처리 

def square(array, B): # 제곱처리하기 
    if B == 1:
        for i in range(N):
            for j in range(N):
                array[i][j] %= 1000
        return array
    
    s_array = square(array, B//2)
    if B % 2 == 0: # 짝수 (B//2)*(B//2)
        return multiply(s_array, s_array)
    else: # 홀수 (B//2)*(B//2)*1
        return multiply(multiply(s_array, s_array), array)
 
def multiply(C, D): # 행렬 곱셈 연산 
    temp = [[0]*N for _ in range(N)] # 크기는 어처피 N*N 행렬
    
    for row in range(N):
        for col in range(N):
            element = 0 
            for i in range(N):
                element += C[row][i] * D[i][col]
            temp[row][col] = element%1000
    return temp

result = square(array, B)   

for i in result:
    print(*i)