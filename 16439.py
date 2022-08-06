# https://www.acmicpc.net/problem/16439 치킨치킨치킨 
from itertools import combinations

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
result = 0 

for a, b, c in combinations(range(m), 3):
    temp_sum = 0 
    for i in range(n):
        temp_sum += max(array[i][a], array[i][b], array[i][c])
    result = max(temp_sum, result)
print(result)