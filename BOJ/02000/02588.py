A = input()
B = input()

len_B = len(B)
for i in range(len_B-1, -1, -1):
  num = int(A)*int(B[i])
  print(num)
print(int(A) * int(B))