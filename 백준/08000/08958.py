count = int(input())
list_score = []
for i in range(count):
    number = input()
    yes_count = 0
    score = 0
    for j in number:
        if j == 'X':
            yes_count = 0
        else:
            yes_count += 1
            score = score + yes_count
    print(score)