def solution(survey, choices):
    personality_type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    result = dict()

    for p_t in personality_type:
        result[p_t] = 0

    for s, c in zip(survey, choices):
        n = int(c) - 4
        l, r = list(s)
        if c < 0:
            result[l] -= n
        elif c > 0:
            result[r] += n
    rt = 'R' if result.get('R') >= result.get('T') else 'T'
    cf = 'C' if result.get('C') >= result.get('F') else 'F'
    jm = 'J' if result.get('J') >= result.get('M') else 'M'
    an = 'A' if result.get('A') >= result.get('N') else 'N'
    return rt + cf + jm + an