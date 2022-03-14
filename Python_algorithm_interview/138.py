# 파이썬 알고리즘 인터뷰 
from collections import deque

# deque 자료구조형을 이용한 풀이  
class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque()
        
        for char in s:
            if char.isalnum():
                q.append(char.lower())
    
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True 
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in s:
            if i.isalnum():
                string.append(i.lower())

        while len(string) > 1:
            if string.pop(0) != string.pop():
                return False
        return True 
