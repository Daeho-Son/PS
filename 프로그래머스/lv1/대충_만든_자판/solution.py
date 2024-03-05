def solution(keymap, targets):
    mapper = dict()
    for keys in keymap:
        for i, key in enumerate(keys, start=1):
            if key in mapper:
                if i < mapper.get(key):
                    mapper[key] = i
            else:
                mapper[key] = i

    answer = []
    for target in targets:
        count = 0
        for c in target:
            if c not in mapper:
                count = -1
                break
            count += mapper.get(c)
        answer.append(count)
    return answer