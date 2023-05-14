#125. Valid Palindrome
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_string = re.sub(r'[\W_]+', '', s).lower()
        
        
        n = len(a_string)
        
        for i in range(n):
            j=n-i-1
            if a_string[i] != a_string[j]:
                return False
                
        return True
        

s = Solution()
print(s.isPalindrome("ab_a"))
