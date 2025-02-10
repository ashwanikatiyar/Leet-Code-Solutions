class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack: 
                    stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
