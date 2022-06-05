N = input()
mid = len(N)//2
sum1 = 0
for i in list(N[:mid]):
    sum1 += int(i)
sum2 = 0
for i in list(N[mid:]):
    sum2 += int(i)
if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')
#이코테 코드
'''
n = input()
length = len(n)
summary = 0

#왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

#오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

if summary = 0:
    print('LUCKY')
else:
    print('READY')
'''