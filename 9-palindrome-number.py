#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        tmp = 0
        
        while tmp < x:
            tmp = (tmp*10) + x % 10
            if x <= tmp:
                break
            x = (x - x % 10) / 10
            
        return tmp == x