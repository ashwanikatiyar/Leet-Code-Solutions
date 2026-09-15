class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl , nl = len(haystack) , len(needle)
        i = 0

        if nl > hl:
            return -1 

        while i+nl <= hl:
            if haystack[i:i+nl] == needle:
                return i
            i+=1
        return -1


