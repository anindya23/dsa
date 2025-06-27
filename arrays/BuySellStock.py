from typing import List

class BuySellStock:
    def maxProfit(self, stocks: List[int]) -> int:
        profit, i, j = 0, 0, 1
        while(i<j):
            if stocks[i] > stocks[j]:
                i, j = i+1, j+1
                continue

            if i < j and ((stocks[j] - stocks[i]) > profit):
                profit = stocks[j] - stocks[i]
                j += 1
                continue
            i = i+1
            j = i+1

        return profit
