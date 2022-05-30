#런타임 에러
'''a, b = map(int, input().split())

min = []
max = []
result = []
result2 = []
cnt = 1
cnt2 = 1


while a*cnt<10000 or b*cnt<10000:
    if a%cnt == 0 and b%cnt == 0:
        min.append(cnt)
    cnt += 1

for i in min:
    max.append(a*i)
    max.append(b*i)

while a*cnt2<10000 or b*cnt2<10000:
    if a*cnt2 in max:
        result.append(a*cnt2)
    if b*cnt2 in max:
        result.append(b*cnt2)
    cnt2 += 1

for j in range(len(result)):
    c = result.pop(0)
    if c in result:
        result2.append(c)


print(min[-1])
print(result2[0])'''
# 유클리드 호제법(https://velog.io/@junyp1/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95)
a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))