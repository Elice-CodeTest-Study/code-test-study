count = int(input())

for _ in range(t):
    input_list = list(input())
    count = 0
    for i in input_list:
        if i == '(':
            count = count + 1
        elif i == ')':
            count = count - 1
        if count < 0:
            print('NO')
            break
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')
