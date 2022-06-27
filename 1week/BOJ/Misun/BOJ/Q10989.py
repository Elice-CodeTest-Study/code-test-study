# 메모리 초과
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

arr.sort()

for i in arr:
    print(i)

# 정답
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for _ in range(n):
    a = int(input())
    arr[a] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

#print는 pypy3에서 차이가 크지만 python 3에서는 크지 않다.