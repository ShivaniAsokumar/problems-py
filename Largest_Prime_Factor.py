""" 
!PROMPT: What is the largest prime factor of the number 600851475143 ?

TODO: Understand
* The prime factors of 13195 are 5, 7, 13 and 29.
* Prime number => Has only 1 and itself as a factor

40: 2, 5 => 5 is the biggest prime factor

TODO: Match
* Count Primes
* Check if a number is prime

if the number is divisible by any number from 2 - num-1: return False
else: return True

TODO: Problem Solving

def largest_prime_factor(num):
  i = 2
  isPrime = True
  while i < num:
    if num is divisible by i:
      for n in range(i):
        if i is divisible by n:
          isPrime = False
      if isPrime:
        add i to array
  return last element in array

"""


def largest_prime_factor(num):
  prime_factors = []
  potential_prime = 2

  while potential_prime <= num:
    if num % potential_prime == 0:
      num /= potential_prime
      prime_factors.append(potential_prime)
    else:
      potential_prime += 1
  
  return prime_factors[-1]


print(largest_prime_factor(5))

# 60/2 = 30/2 = 15/3 = 5/5

