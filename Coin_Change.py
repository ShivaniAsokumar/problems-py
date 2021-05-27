""" 
!PROMPT: This function will determine the fewest coin are needed to reach the total in amount given the denominations in coins. 

TODO: Understand
* Input => amount (Integer) and coins (Integer)
* Output => calculate the fewest number of coins that you need to make up the sum

? Can you expect to see empty array of coins, and what should you do then

? Is the coins array always sorted

"""

def coin_change(amount, coins):
    # If the length of coin = 1 and value is less than the amount, return -1
    if len(coins) == 1 and coins[0] < amount:
        return -1
    

