# a, c, g, t
needs = [0, 0, 0, 0]


def is_password(dna_counter):
    for dna_word, need in zip(['A', 'C', 'G', 'T'], needs):
        if dna_counter.get(dna_word) < need:
            return False
    return True


def main():
    global needs
    answer = 0
    s, p = map(int, input().split())
    dna_str = input()
    needs = list(map(int, input().split()))

    start_index = 0
    dna_counter = dict(zip(['A', 'C', 'G', 'T'], [0] * 4))
    for c in dna_str[:p]:
        dna_counter[c] += 1
    if is_password(dna_counter):
        answer += 1
    for c in dna_str[p:]:
        start_c = dna_str[start_index]
        dna_counter[start_c] -= 1
        dna_counter[c] += 1
        start_index += 1
        if is_password(dna_counter):
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
