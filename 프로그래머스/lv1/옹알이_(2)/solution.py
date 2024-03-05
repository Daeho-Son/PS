def solution(babbling):
    answer = 0
    pronounces = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for p in pronounces:
            if p * 2 in b:
                break
            b = b.replace(p, '0')
        else:
            if b.isdigit():
                answer += 1
    return answer
