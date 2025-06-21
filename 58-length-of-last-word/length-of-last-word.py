class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s) - 1
        size = 0

        while length >= 0 and s[length] == " ":
            length -= 1

        while length >= 0 and s[length] != " ":
            size += 1
            length -= 1

        return size
        