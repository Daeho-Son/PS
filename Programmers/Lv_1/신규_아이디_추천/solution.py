def solution(new_id):
    answer = ''
    index = -1
    while index < len(new_id) - 1:
        index += 1
        c = new_id[index].lower()
        if not c.isalpha() and not c.isdigit() and c not in ['-', '_', '.']:
            continue
        if answer and answer[-1] == '.' and c == '.':
            continue
        if not answer and c == '.':
            continue
        answer += c
    if not answer:
        answer += 'a'
    answer = answer[:15]
    while answer and answer[-1] == '.':
        answer = answer[:-1]
    while answer and len(answer) <= 2:
        answer += answer[-1]
    return answer
