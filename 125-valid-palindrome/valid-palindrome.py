class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        new = ""

        for char in s:
            if char.isalnum():
                new += char
        l = 0
        r = len(new) - 1
        while l < r:
            if new[l] == new[r]:
                l += 1
                r -= 1
                
            else:
                return False

        return True

        