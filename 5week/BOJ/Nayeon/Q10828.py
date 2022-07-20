import sys
input = sys.stdin.readline # input => 시간 초과 

n = int(input())
stack = []

for i in range(n):
    s = input().split()
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif s[0] == 'top':
        if len(stack) > 0: print(stack[-1]) # 가장 맨위
        else: print(-1)
    elif s[0] == 'pop':
        if len(stack) > 0: print(stack.pop()) #가장 마지막 원소 제거
        else: print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty': 
      # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stack) > 0: print(0)
        else: print(1)






        