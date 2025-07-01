class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        store = 0
        rev = 0
        y = x

        if len(str(x))==1:
            return True

        for i in range(len(str(x))):
            store = x%10
            rev = rev*10 + store
            x = x//10
        if(rev == y):
            return True
        else:
            return False
        
        