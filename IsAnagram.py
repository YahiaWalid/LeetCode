#242. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns = len(s)
        nt = len(t)

        if ns != nt:
            return False


        count_s={}
        count_t={}

        for i in range(ns):
            count_s[s[i]] = 1 + count_s.get(s[i],0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for letter in s:
            if count_s[letter] != count_t.get(letter,0):
                return False

        return True


s = Solution()

print(s.isAnagram("anagram","nagaram"))
