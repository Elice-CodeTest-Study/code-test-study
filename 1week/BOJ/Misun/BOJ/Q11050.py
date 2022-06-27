# 이항 계수 nCk = n!/k!(n-k)!

from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)