n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = 0

while True:
    if m == 0:
        break
    for i in range(k):
        result += arr[n-1]
        m -= 1
    if m == 0:
        break
    result += arr[n-2]
    m -= 1

print(result)