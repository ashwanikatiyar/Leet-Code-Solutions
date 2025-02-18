class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = 1  # Start numbering from 1
        
        for ch in pattern:
            stack.append(num)
            num += 1
            if ch == 'I':  # When 'I' is encountered, pop the stack
                while stack:
                    result.append(str(stack.pop()))
        
        stack.append(num)  # Append the last number
        while stack:
            result.append(str(stack.pop()))
        
        return ''.join(result)
