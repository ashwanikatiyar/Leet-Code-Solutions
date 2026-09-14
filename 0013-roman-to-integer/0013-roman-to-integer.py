class Solution:
    def romanToInt(self, s: str) -> int:
        valueMap = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        total = 0
        n = len(s)
        i = n - 1


        while i >= 0 :
            if i > 0 and valueMap[s[i]] > valueMap[s[i-1]]:
                total += valueMap[s[i]] - valueMap[s[i-1]]
                i -= 2
            else:
                total += valueMap[s[i]]
                i-=1
        return total
