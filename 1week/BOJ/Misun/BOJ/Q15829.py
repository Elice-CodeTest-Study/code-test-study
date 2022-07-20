n = int(input())
str1 = input()
answer = 0

for i in range(n):
    answer += (ord(str1[i]) - 96) * (31 ** i)

print(answer % 1234567891)

# a부터 z까지를 1부터 26까지로 표현하는 문제 형식은 ord(a) - 96을 이용하자