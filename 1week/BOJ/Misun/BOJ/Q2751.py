#시간 초과
'''n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

tup = tuple(sorted(arr))

for j in tup:
    print(j)'''

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

for j in sorted(arr):
    print(j)