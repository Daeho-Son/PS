distance = {2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4],
            5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3],
            8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2],
            0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1]}


def press_keypad(n, current_l, current_r, hand):
    if n in [1, 4, 7]:
        return 'L'
    if n in [3, 6, 9]:
        return 'R'
    distance_from_l_to_n = distance[n][current_l]
    distance_from_r_to_n = distance[n][current_r]
    if distance_from_l_to_n < distance_from_r_to_n:
        return 'L'
    elif distance_from_l_to_n > distance_from_r_to_n:
        return 'R'
    return 'L' if hand == 'left' else 'R'


def solution(numbers, hand):
    answer = ''
    current_pos = {'L': 10, 'R': 11}

    for number in numbers:
        current_l = current_pos['L']
        current_r = current_pos['R']
        l_or_r = press_keypad(number, current_l, current_r, hand)
        answer += l_or_r
        current_pos[l_or_r] = number
    return answer
