#1929. Concatenation of Array


class Solution(object):

    
    def getConcatenation1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = [0] * (2 * n)

        j=0
        for i in range(n):
            ans[j] = nums[i]
            ans[j + n] = nums[i]
            j=(j+1)%n

        return ans


    #another method
    def getConcatenation2(self,nums):
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans



s = Solution()
sol = s.getConcatenation2([1,2,3])
print(sol)
