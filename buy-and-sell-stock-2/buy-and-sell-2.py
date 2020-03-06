# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


# Maximal solution equates to iterating over successive
# points and when a peak follows a valley, increment profit
def maximize_profit(prices):
    max_profit = 0
    index = 1
    while index < len(prices):
        price = prices[index]
        if price > prices[index - 1]:
            max_profit += price - prices[index - 1]
        index += 1
    return max_profit


# Brute force - get all possible transactions
# def maximize_profit(prices):
#     return calculate_profit(prices, 0)

# def calculate_profit(prices, index):
#     if index >= len(prices):
#         return 0
#     max_profit, start = 0, index
#     while start < len(prices):
#         current_max, i = 0, start + 1
#         while i < len(prices):
#             # buying at current and selling at all possible combinations after
#             if prices[start] < prices[i]:
#                 profit = calculate_profit(prices, i + 1) + prices[i] - prices[start]
#                 if profit > current_max:
#                     current_max = profit
#             i += 1
#         if current_max > max_profit:
#             max_profit = current_max
#         start += 1
#     return max_profit


def test_1():
    assert (maximize_profit([7, 1, 5, 3, 6, 4]) == 7)


def test_2():
    assert (maximize_profit([1, 2, 3, 4, 5]) == 4)


def test_3():
    assert (maximize_profit([7, 6, 4, 3, 1]) == 0)
