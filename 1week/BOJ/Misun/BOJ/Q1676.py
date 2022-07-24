# n!의 끝에 나오는 0의 개수를 계산
from math import factorial
n = int(input())
cnt = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)