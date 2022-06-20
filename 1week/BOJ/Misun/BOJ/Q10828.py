n = int(input())
stack = []

for i in range(n):
    inputType = input()
    if inputType.split()[0] == "push":
        stack.append(inputType.split()[1])
    elif inputType == "top":
        if len(stack) != 0:
            print(stack[-1])
        elif len(stack) == 0:
            print(-1)
    elif inputType == "size":
        print(len(stack))
    elif inputType == "empty":
        if len(stack) != 0:
            print(1)
        elif len(stack) == 0:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())