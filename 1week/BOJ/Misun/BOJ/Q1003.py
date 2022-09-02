# 재귀로 풀면 시간 초과
dec = [0, 0]

def fibo(n):
    if n==0:
        dec[0] += 1
    elif n==1:
        dec[1] +=1
    else:
        fibo(n-1)
        fibo(n-2)

T = int(input())

for _ in range(T):
    a = int(input())
    fibo(a)
    print(dec[0], dec[1])
    dec = [0, 0]

# 해결
# 0의 갯수 = 이전 1의 갯수, 1의 갯수 = 이전 0 + 이전 1 개수
t = int(input())
 
for _ in range(t):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1]) 
 
    print(cnt_0[n], cnt_1[n])