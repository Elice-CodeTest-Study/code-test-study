n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])

arr = sorted(arr, key=lambda x:(x[0], x[1])) # 첫번째 기준, 두번째 기준 우선순위로 정렬

for i in arr:
    print(i[0],i[1])