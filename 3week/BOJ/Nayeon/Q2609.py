a, b = map(int, input().split())

def gcd(a,b):
    while b: #b가 0이 될 때까지 반복!
        a, b = b, a%b 
    return a 

print(gcd(a, b))
# 최소 공배수
print((a*b)//gcd(a,b))    

## 2번째 방법
# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))