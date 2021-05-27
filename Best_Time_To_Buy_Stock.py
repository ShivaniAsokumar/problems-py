""" 
!PROMPT: Say you have an array prices for which the ith element is the price of a given stock on day i.Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

* Must sell before buying again

TODO: Understand
* Goal is to make the most profit by buying and selling stock

Given an array, take each element and compare with every other element after (nested loops).

TODO: Problem Solving

def Best_Time...: 
  profit = 0
  for i in range(len(list) - 1):
    if i > i + 1:
      dont sell
    if i < i + 1:
      sell (profit += i+1 - i)

  return profit

"""

def Best_Time_To_Buy_Stock(prices):
  profit = 0
  for i in range(len(prices) - 1):
    if prices[i] < prices[i+1]:
      profit += (prices[i+1] - prices[i])

  return profit

print(Best_Time_To_Buy_Stock([7,6,4,3,1]))

""" 
TODO: Evaluate
Complexity = O(n)
"""