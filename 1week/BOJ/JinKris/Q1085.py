x,y,w,h = input().split()
list = [int(x)-0,int(w)-int(x),int(y)-0,int(h)-int(y)]
print(min(list))