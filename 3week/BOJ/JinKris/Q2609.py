a, b = map(int, input().split())

#유클리드  호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))


#파이썬  내장 함수
# import math

# print(math.gcd(a, b))
# print(math.lcm(a, b))