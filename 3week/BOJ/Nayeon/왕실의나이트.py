#L자 형태로만 이동가능
# 수평 2칸 -> 수직 1칸
# 수직 2칸 -> 수평 1칸
#정원 밖으로 못 나감!
# 현재의 위치를 입력하면 -> 움질일수 있는 경우의 수 출력! 

n = input()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1 # a =1 , b=2, c=3 ...
move = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(-1,-2),(1,-2),(1,2)]
cnt = 0

for x, y in move:
    r = row + x
    c = col + y
    if r >= 1 and r <=8 and c >=1 and c <= 8:
        cnt += 1

print(cnt)
