# https://www.acmicpc.net/problem/16439 치킨치킨치킨 
from itertools import combinations

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
result = 0 
if n <= 3:
    for i in range(n):
        result += max(array[i])
else:

print(result)
    