count = int(input())
for i in range(count*2):
    if i%2 == 0:
        print('* '*(count-count//2))
    else:
        print(' *'*(count//2))