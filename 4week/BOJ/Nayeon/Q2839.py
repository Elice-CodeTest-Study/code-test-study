num = int(input())
count = 0

while num >=0: # print(-1) 을 작성하기 위해
    if num % 5 == 0 : #5의 배수
        count += (num // 5)
        print(count)
        break
    else:
        num -= 3
        count += 1 
else:
    print(-1)
        