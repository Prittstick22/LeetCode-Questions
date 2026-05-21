class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0
        y = 0
        longest = 0
        seen = []

        while y < len(s):

            if s[y] in seen:

                while s[x] != s[y]:
                    seen.remove(s[x])
                    x += 1

                seen.remove(s[x])
                x += 1

            seen.append(s[y])

            currentLength = y - x + 1

            if currentLength > longest:
                longest = currentLength

            y += 1

        return longest