def get_divisor(number):
    divisor = list()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisor.append(i)
            divisor.append(number // i)
    return len(set(divisor))


def solution(number, limit, power):
    answer = 0
    for knight in range(number+1):
        damage = get_divisor(knight)
        answer += power if damage > limit else damage
    return answer
