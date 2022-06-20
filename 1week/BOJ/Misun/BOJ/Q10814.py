n = int(input())
arr = []

for _ in range(n):
    a, b = input().split()
    a = int(a)
    arr.append((a, b))

arr.sort(key = lambda x:x[0])

for i in arr:
    print(i[0], i[1])

'''이 문제에서 짚고 넘어가야 하는 점은, stable 정렬과 unstable 정렬 방식이다.
stable 정렬은 말 그대로 안정 정렬이다. 안정 정렬에서는 입력 받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지한다.
예를 들어, [1, 2, 3(X), 4, 5, 3(Y)] 을 오름차순 정렬한다면, [1, 2, 3(X), 3(Y), 4, 5]순으로 세 번째 위치한 3의 위치와 여섯 번째 위치한 3의 위치가 바뀌지 않는다. unstalbe 정렬에서는 이러한 정렬을 장담할 수 없다.
파이썬은 기본적으로 stalbe 정렬을 한다는 점을 알아두면 좋다.'''