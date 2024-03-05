def convert_number_to_base_number(number, base):
    base_chars = "0123456789ABCDEF"[:base]
    base_number = ''
    while number > 0:
        number, mod = divmod(number, base)
        base_number += str(base_chars[mod])
    return base_number[::-1] if base_number else str(0)


def solution(n, t, m, p):
    string = ''
    current_number = 0
    while len(string) < t * m:
        string += convert_number_to_base_number(current_number, n)
        current_number += 1
    return ''.join([string[i] for i in range(p-1, t*m, m)])

