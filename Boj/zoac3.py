# https://www.acmicpc.net/problem/20436 zoac3

left, right = input().split()
word = input()
# 택시거리를 구하기 
keyboard = ['qwertyuiop',
            'asdfghjkl',
            'zxcvbnm']

# 자음쪽 -> 왼손 모음쪽 -> 오른손
mo = 'yuiophjklbnm'

# keyboard row 에 있는지 검사 -> column 에서 index() 함수 써서 위치 반환하기 

def pos_check(alphabet):
    a_x, a_y = -1, -1 
    for i in range(len(keyboard)):
        if alphabet in keyboard[i]:
            a_x = i 
            for j in range(len(keyboard[i])):
                if keyboard[i][j] == alphabet:
                    a_y = j 
    
    return a_x, a_y 

left_x, left_y = pos_check(left)
right_x, right_y = pos_check(right)
result = 0 

for i in range(len(word)):
    word_x, word_y = pos_check(word[i])
    result += 1 
    if word[i] in mo: # right 
        result += abs(right_x - word_x) + abs(right_y - word_y)
        right_x, right_y = word_x, word_y 
        
    else: # left 
        result += abs(left_x - word_x) + abs(left_y - word_y)
        left_x, left_y = word_x, word_y 
    
print(result)