count = int(input())
score = list(map(int, input().split()))
max_score = max(score)

list_change_score = []
for i in score:
    list_change_score.append((i/max_score)*100)

print(sum(list_change_score)/len(list_change_score))