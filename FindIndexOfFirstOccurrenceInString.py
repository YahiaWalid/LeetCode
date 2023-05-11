#28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_haystack = len(haystack)
        n_needle = len(needle)


        for i in range(n_haystack):
            if (i+n_needle) <= n_haystack :
                if haystack[i:i+n_needle] == needle:
                    return i

        return -1


s = Solution()

print(s.strStr("hello","ll"))
