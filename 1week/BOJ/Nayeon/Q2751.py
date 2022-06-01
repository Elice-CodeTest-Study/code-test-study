# 수 정렬하기.
# 퀵 정렬, 선택 정렬, 삽입 정렬 모두 시간 초과  ->Pypy3 사용해서 해결 or 병합 정렬 

n=int(input())
num=[]

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)