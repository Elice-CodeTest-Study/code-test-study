# dfs -> 실패
t = int(input())

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < m):
            if table[nx][ny] == 1:
                table[nx][ny] = -1
                dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    table = [[0]* m for _ in range(n)]
    result = 0

    for _ in range(k):
        w, h = map(int, input().split())
        table[h][w] = 1

    for i in range(n):
        for j in range(m):
            if table[i][j] > 0:
                dfs(i, j)
                result += 1

    print(result)

# bfs
t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0
                cnt += 1
    print(cnt)