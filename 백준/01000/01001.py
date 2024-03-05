a, b = map(int, input().split())

if 0 >= a or b >= 10:
  a, b = map(int, input().split())
else:
  print(a - b)