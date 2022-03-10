# 파이썬 알고리즘 인터뷰 

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
        