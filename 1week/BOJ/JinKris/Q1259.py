while True:
  num = input()
  if(num=='0') :
    break
  num = list(num)
  revNum = num[::-1]
  print('yes') if num==revNum else print('no')