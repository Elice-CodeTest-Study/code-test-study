#모든 모험가를 모험 보낼 때
'''n = int(input())
member = list(map(int, input().split()))
result = 0

member.sort()

while len(member) != 0:
    max = member[len(member)-1]
    for i in range(1, max+1):
        member.pop(len(member) - i)
    result += 1

print(result)'''

#최대한의 그룹
n = int(input())
member = list(map(int, input().split()))
member.sort()
result = 0
count = 0
for i in member:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)