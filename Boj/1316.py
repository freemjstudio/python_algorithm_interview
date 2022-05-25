# 1316 그룹단어 체커

n = int(input())
count = n

for _ in range(n):
    word = input() 
    array = []
    
    for i in range(0, len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:] # 현재 글자 이후 문자열을 새로 생성
            if new_word.count(word[i]) > 0: # 남은 글자 중에 현재 글자가 있었다면 
                count -= 1 # 그룹 단어가 아니므로 count -= 1
                break 
    
print(count)