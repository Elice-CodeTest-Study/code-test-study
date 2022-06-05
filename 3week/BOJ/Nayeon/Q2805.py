
n, m = map(int, input().split())
trees = list(map(int, input().split))
start, end = 0, sum(trees)

#이분탐색
while start <= end:  
    mid = (start + end) // 2
    cnt = 0 # 잘린 나무 수
    for tree in trees:
            if tree > mid: 
                cnt += tree - mid
    if  cnt  >=  mid:
        start = mid + 1 # 
    else:
        end = mid-1   #          

print(end)

