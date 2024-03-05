"""
# 시도 1.
## 의사 코드 - 작성해보라는 조언을 받아서 작성함

선물 지수 = 이번 달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수

if A와 B가 선물을 주고 받은 기록이 있다면:
    if A가 B에게 선물을 더 많이 줬다면:
        B가 A에게 선물 + 1
    else:
        A가 B에게 선물 + 1
if A와 B가 선물을 주고 받은 기록이 없다면 or 선물을 주고 받은 수가 같다면:
    if A의 선물 지수 == B의 선물 지수:
        continue
    if A의 선물 지수가 B의 선물 지수보다 크다면:
        B가 A에게 선물 + 1
    else:
        A가 B에게 선물 + 1
"""
from itertools import combinations


def solution(friends, gifts):
    friends_count = len(friends)
    answer = dict(zip(friends, [0 for _ in range(friends_count)]))
    gift_send_history = dict(zip(friends, [[] for _ in range(friends_count)]))
    gift_receive_history = dict(zip(friends, [[] for _ in range(friends_count)]))
    gift_indices = dict(zip(friends, [0 for _ in range(friends_count)]))
    for gift in gifts:
        sender, receiver = gift.split()
        gift_send_history[sender].append(receiver)
        gift_receive_history[receiver].append(sender)
        gift_indices[sender] += 1
        gift_indices[receiver] -= 1
    for a, b in combinations(friends, 2):
        a_to_b = gift_send_history[a].count(b)
        b_to_a = gift_send_history[b].count(a)
        if (a_to_b or b_to_a) and a_to_b != b_to_a:
            if a_to_b > b_to_a:
                answer[a] += 1
            else:
                answer[b] += 1
        else:
            if gift_indices[a] == gift_indices[b]:
                continue
            if gift_indices[a] > gift_indices[b]:
                answer[a] += 1
            else:
                answer[b] += 1
    return max(answer.values())
