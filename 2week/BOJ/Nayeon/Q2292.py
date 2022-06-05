#벌집
num = int(input())
count = 1 
first = 1 

while num > first:
    first+=6*count
    count+=1

print(count)   