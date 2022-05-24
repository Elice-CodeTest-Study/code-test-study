#분해합
target = int(input())
 
for i in range(1, target):
    temp = sum(map(int, str(i)))
    print(temp)
    result = i + temp
    if result == target:
        print(i)
        break
else:
    print(0)