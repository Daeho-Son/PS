sum_score = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    sum_score = sum_score + score

print(sum_score//5)