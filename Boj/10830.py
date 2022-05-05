# 10830 행렬 제곱 

N, B = map(int, input().split())
array = []
result = []
for _ in range(N):
    array.append(list(map(int, input().split())))

# 홀수 , 짝수 처리 

 
def square():
    for row in range(N):
        for col in range(N):
            element = 0 
            for i in range(N):
                element += array[row][i] * array[i][col]
            
for i in result:
    print(*i)