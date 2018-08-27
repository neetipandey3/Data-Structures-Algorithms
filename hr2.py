class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        i = 0
        profit = 0
        if prices:
            buy_at = prices[0]
        while i < len(prices):

            j = i + 1
            if j == len(prices):
                return max_profit + profit
            if buy_at < prices[j]:
                buy_at = min(prices[i], buy_at)
                sell_at = prices[j]

            else:
                buy_at = prices[j]
                sell_at = prices[j]


            if profit > sell_at - buy_at:
                max_profit += profit
                profit = 0
                i += 1
                buy_at = prices[j]
                continue
            i += 1
            profit = sell_at - buy_at
        return max_profit



def main():
    s = Solution()
    print(s.maxProfit([1,2,3,4,5]))

if __name__ == "__main__":
    main()