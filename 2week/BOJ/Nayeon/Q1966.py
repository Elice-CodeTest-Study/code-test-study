test = int(input())
 
for _ in range(test):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    index = [0 for _ in range(n)]
    index[m] = 1  
    cnt = 0
    
    while p:
        if p[0] == max(p):  
            cnt += 1
            if index[0] == 1:
                print(cnt)
                break
            p.pop(0)
            index.pop(0)
        else:
            p.append(p.pop(0))
            index.append(index.pop(0))

