T = int(input())
total = []
for i in range(1, T+1):
    A, B = map(int, input().split())
    if 0<A or B<10:
        total.append(A+B)
    else:
        A, B = map(int, input())

for i in total:
    print(i)
