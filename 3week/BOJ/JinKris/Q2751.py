#빠른 정렬 하고싶다면 .. 퀵,머지 등.. 하지만 파이썬 sort로 충분히 가능
import sys

N = int(input())
arr = []
for i in range(N) : 
	arr.append(int(sys.stdin.readline()))
   
arr.sort()
for i in arr: 
	sys.stdout.write(str(i) + "\n")

    
# 힙 정렬
# import heapq
# import sys
# def input():
# 	return int(sys.stdin.readline())
# def print(v):
# 	sys.stdout.write(str(v)+'\n')
# data = [input() for _ in range(input())]
# heapq.heapify(data)
# [print(heapq.heappop(data)) for _ in range(len(data))]