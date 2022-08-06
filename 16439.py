# https://www.acmicpc.net/problem/16439 치킨치킨치킨 
from itertools import combinations

n, m = map(int, input().split())
array = []
chicken = [i for i in range(0, m)]
for i in range(n):
    array.append(list(map(int, input().split())))
result = 0 
if n <= 3:
    for i in range(n):
        result += max(array[i])
else:
    comb = combinations(chicken, 3) # 3가지 종류만 주문할 수 있음 
    for data in comb:
        temp = []
        temp_result = 0
        for index in data:
            for i in range(n):
                temp.append(array[i][index])
        temp.sort(reverse=True)
        for i in range(n):
            temp_result += temp[i]
    result = max(result, temp_result)
            
print(result)
    