count = int(input())
for i in range(count):
    repeat, char = input().split()
    for j in char:
        print(j*int(repeat), end='')
    print()