# 10867 중복 빼고 정렬하기 

n = int(input())
data = list(map(int, input().split()))

data.sort()
data = set(data)
print(*data)