n = int(input())
arr = list(str, map(input().split()))
current = [1,1]

for a in arr:
    if a =='L':
        if current[1] >1: # 정사각형 공간을 벗어나는 움직임 check 하기 위해
            current[1]-=1
    elif a=='R':
        if current[1]<n:
            current[1]+=1
    elif a=='U':
        if current[0]>1:
            current[0]-=1
    elif i=='D':
        if current[1]<n:
            current[0]+=1

print(current[0],current[1])