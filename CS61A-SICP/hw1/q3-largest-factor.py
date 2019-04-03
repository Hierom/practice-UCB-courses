from math import floor, sqrt
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """    
    max_factor = 1
    for i in range(2,floor(sqrt(n))+1):
      if n % i == 0:
        return max(max_factor, n // i)
    return max_factor
