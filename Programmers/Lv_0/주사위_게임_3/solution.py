from collections import Counter


def solution(a, b, c, d):
    dice_set = {a, b, c, d}
    dice_type_count = len(dice_set)
    if dice_type_count == 1:
        return 1111 * a
    elif dice_type_count == 2:
        dice_type_list = list(dice_set)
        if [a, b, c, d].count(dice_type_list[0]) == 3:
            p, q = dice_type_list
            return (10 * p + q) ** 2
        elif [a, b, c, d].count(dice_type_list[1]) == 3:
            q, p = dice_type_list
            return (10 * p + q) ** 2
        else:
            p, q = dice_type_list
            return (p + q) * abs(p - q)
    elif dice_type_count == 3:
        q, r = [dice for dice in dice_set if [a, b, c, d].count(dice) != 2]
        return q * r
    elif dice_type_count == 4:
        return min([a, b, c, d])
