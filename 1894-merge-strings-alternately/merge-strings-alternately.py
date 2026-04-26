class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        target = ""
        while True:
            target += word1[pointer1]
            target += word2[pointer2]
            pointer1 +=1
            pointer2 +=1
            if len(word1) == len(word2) and pointer2 == len(word2):
                return target
            if pointer1 == len(word1):
                target += word2[pointer2:]
                return target
            if pointer2 == len(word2):
                target += word1[pointer1:]
                return target


        