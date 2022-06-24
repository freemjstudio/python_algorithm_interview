# 서강그라운드 14938

n, m, r = map(int, input().split()) # 지역의 개수, 수색범위, 길의 개수 
item = list(map(int, input().split())) # 아이템의 수 
for _ in range(r):
    a, b, l = map(int, input().split()) # 길 양끝에 존재하는 지역의 번호, 길이
    
