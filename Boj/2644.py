n = int(input())
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람
m = int(input()) # edges case
for _ in range(m):
    x, y = map(int, input().split()) # 부모 - 자식 
    