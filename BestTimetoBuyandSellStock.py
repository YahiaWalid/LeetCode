#121. Best Time to Buy and Sell Stock

class Solution(object):

    # bad time complexity
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        n = len(prices)

        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i]>max:
                    max = prices[j]-prices[i]

        return max


    # linear time complexity
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x=0

        min = prices[0]
        for price in prices:
            if price < min:
                min = price
            x = max(x,price-min)

        return x



s = Solution()
sol = s.maxProfit2([7,1,5,3,6,4])
print(sol)
