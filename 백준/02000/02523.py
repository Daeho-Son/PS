count = int(input())

for i in range(1, (2*count)):
    if i > count:
        print('*'*(2*count-i))
    else:
        print('*'*i)