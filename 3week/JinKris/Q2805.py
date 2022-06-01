N,M = map(int,input().split())
arr = list(map(int,input().split()))

def solution(arr,start,end):
  res = 0
  while start<=end:
    mid = (start+end)//2
    total = 0
    for x in arr:
      if x>mid:
        total +=x-mid

    if total<M:
      end = mid -1
    else:
      res = mid
      start = mid+1
  return res

result = solution(arr,0,max(arr))
print(result)