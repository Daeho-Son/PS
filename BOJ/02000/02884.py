H, M = map(int, input().split());
x = H*60 + M - 45
print((x//60)%24, x%60)