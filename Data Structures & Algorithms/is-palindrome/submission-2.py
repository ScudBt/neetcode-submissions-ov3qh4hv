class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case-insensitive and ignore non-alphanumeric chars
        newS = ''
        for c in s:
            if c.isalnum():
                newS += c.lower()
        for i in range(len(newS)//2):
            if newS[i] != newS[len(newS) - i -1]:
                return False
        return True