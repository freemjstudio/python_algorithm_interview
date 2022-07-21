# https://www.acmicpc.net/problem/20436 zoac3
import itertools

left, right = input().split()
word = input()
# 택시거리를 구하기 
keyboard = ['qwertyuiop',
            'asdfghjkl',
            'zxcvbnm']

# keyboard row 에 있는지 검사 -> column 에서 index() 함수 써서 위치 반환하기 
def pos_check(alphabet):
    a_x, a_y = -1, -1 
    for i in range(3):
        if alphabet in keyboard[i]:
            a_x = i 
            for j in range(len(keyboard[i])):
                if keyboard[j] == alphabet:
                    a_y = j 
    
    return a_x, a_y 

left_x, left_y = pos_check(left)
right_x, right_y = pos_check(right)
result = 0 

for i in range(len(word)):
    word_x, word_y = pos_check(word[i])
    if (abs(left_x-word_x)+ abs(left_y-word_y)) < (abs(right_x - word_x)+ abs(right_y - word_y)):
        left_x, left_y = word_x, word_y
        result += abs(left_x-word_x)+ abs(left_y-word_y)
    else:
        right_x, right_y = word_x, word_y
        result += (abs(right_x - word_x)+ abs(right_y - word_y))

print(result)
    
