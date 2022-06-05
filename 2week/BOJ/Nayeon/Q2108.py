import sys 
from collections import Counter

#main
n = int(sys.stdin.readline())

numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
    
print(round(sum(numbers)/n))

def median(nums):
    nums.sort()
    mid = nums[n//2] 
    
    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod
        
def scope(nums):
    return max(nums) - min(nums)

print(median(numbers))
print(mode(numbers))
print(scope(numbers))