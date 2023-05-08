import math
import sys

sys.setrecursionlimit(10**6)  # Set the maximum recursion depth to 1 million


def compute_euler_number(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1

    e = compute_euler_number(n-1, memo) + 1 / math.factorial(n)
    memo[n] = e

    return e


# Compute the Euler number using n = 100
euler_number = compute_euler_number(10000)
print(euler_number)  # Output: 2.7182818284590455
