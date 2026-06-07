class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # 32-bit signed integer
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Skip whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if end
        if i == n:
            return 0
        
        # Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        #Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        #Apply sign 
        return res * sign