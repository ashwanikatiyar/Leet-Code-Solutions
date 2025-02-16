class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        res = [0] * size  # Result sequence initialized with 0
        used = set()  # Set to track used numbers
        
        def backtrack(index):
            if index == size:  # If filled completely, return True
                return True
            
            if res[index] != 0:  # If already filled, move to the next index
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):  # Try larger numbers first for lexicographical order
                if num in used:
                    continue
                if num == 1:  # Number 1 takes only one position
                    res[index] = 1
                    used.add(1)
                    if backtrack(index + 1):  # Move to the next position
                        return True
                    used.remove(1)
                    res[index] = 0
                else:  # Place number `num` at `index` and `index + num`
                    if index + num < size and res[index + num] == 0:
                        res[index] = res[index + num] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        used.remove(num)
                        res[index] = res[index + num] = 0
            
            return False  # If no valid number placement found, backtrack
        
        backtrack(0)  # Start backtracking from index 0
        return res
