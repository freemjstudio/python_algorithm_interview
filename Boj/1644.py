# 소수의 연속합
result = 0 
n = int(input())
check = [True]*(n+1) 
numbers = [] # 소수 인 숫자들의 배열 

for i in range(2, n+1):
    if check[i] == True:
        for j in range(i, n+1, i):
            if check[j] == True:
                check[j] = False

for i in range(2, n+1):
    if check[i] == True:
        numbers.append(i) # 지워지지 않은 숫자는 소수 

# two pointer 알고리즘                 
start = 0
end = 0 

# false 이면 소수
print(result)

