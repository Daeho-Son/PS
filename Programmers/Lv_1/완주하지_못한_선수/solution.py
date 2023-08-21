from collections import Counter


def solution(participant, completion):
    answer = ''
    participant_counter = dict(Counter(participant))
    for c in completion:
        participant_counter[c] -= 1
    for player, count in participant_counter.items():
        if count != 0:
            answer = player
    return answer
