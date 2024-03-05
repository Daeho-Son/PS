from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_number = dict(zip(want, number))
    for idx in range(len(discount)-9):
        discount_counter = Counter(discount[idx:idx+10])
        if sorted(want_number.items()) == sorted(discount_counter.items()):
            answer += 1
    return answer
