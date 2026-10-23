class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        i = 0
        while i < len(s):
            if s[i].isalnum():
                res = res + s[i].lower()
            i += 1
        if res == res[::-1]:
            return True
        else:
            return False
