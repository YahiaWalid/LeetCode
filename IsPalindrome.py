#9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        string = str(x)
        n = len(string)

        for i in range (n):
            if string[i] != string[n-i-1]:
                return False
        return True


s = Solution()

print(s.isPalindrome(12321))
