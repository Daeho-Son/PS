import math


n = int(input())
count = 0
for number in str(math.factorial(n))[::-1]:
    if number != '0':
        break
    count += 1
print(count)