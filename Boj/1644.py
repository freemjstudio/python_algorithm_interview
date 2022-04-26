# 소수의 연속합
count = 0 
n = int(input())
check = [True]*(n+1) 
numbers = [] # 소수 인 숫자들의 배열 

for i in range(2, n+1):
    if check[i] == True:
        numbers.append(i)
        for j in range(i, n+1, i):
            if check[j] == True:
                check[j] = False

# two pointer 알고리즘                 
end = 0 
interval_sum = 0 
for start in range(len(numbers)):
    while interval_sum < n and end < len(numbers):
        interval_sum += numbers[end]
        end += 1
    if interval_sum == n:
        count += 1
    interval_sum -= numbers[start]
    
print(count)

