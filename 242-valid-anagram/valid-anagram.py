class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap [char] = 1
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] == 0:
                    hashmap.pop(char)
            else:
                return False

        if hashmap == {}:
            return True 
            
        return False
        
        
            
            
        