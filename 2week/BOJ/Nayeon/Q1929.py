#소수 구하기.
a,b = map(int, input().split())

for i in range(a,b+1):
   if i == 1: 
        continue #1은 소수가 아님
   for j in range(2, int(i** 0.5)+1 ): 
       # for j in range(2, i): -> 시간초과...뜸....
        if i%j==0:
            break
   else:
        print(i)