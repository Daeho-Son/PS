def solution(s):
    x_count = 0
    not_x_count = 0
    answer = list()
    str = ""
    for c in s:
        str += c
        if str[0] == c:
            x_count += 1
        else:
            not_x_count += 1
        if x_count == not_x_count:
            answer.append(str)
            str = ""
            x_count = 0
            not_x_count = 0
    if str:
        answer.append(str)
    print(answer)
    return len(answer)