# 시간초과
import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())
day = 0	#올라가는 데 걸리는 일수

while 1:
    day+=1
    if a*day-b*(day-1)>=v:
        break
print(day)

#정답
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)