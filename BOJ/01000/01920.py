n = int(input())
a = set(input().split())
m = int(input())
ms = input().split()

for num in ms:
    print(1 if num in a else 0)
