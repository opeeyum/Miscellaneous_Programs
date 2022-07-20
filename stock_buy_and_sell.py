import sys

def maxProfit(prices) -> int:
    # Overall Profit
    op = 0 

    # Least buying price
    lbp = sys.maxsize

    for price in prices:
        if price < lbp:
            lbp = price
        
        # If stock is bought at current price, What will be the current profit
        cur_profit = price - lbp

        # If current profit is more than overall profit then reset the overall profit
        if cur_profit > op:
            # op = max(op, price - lbp)
            # min/max are slower compared to if/else
            op = cur_profit
    return op

prices = [7, 1, 4, 6, 3]
print(maxProfit(prices))