from collections import deque


def is_correct(u):
    stack = []

    for c in u:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
            continue
        stack.append(c)
    if stack:
        return False
    return True


def reverse_bracket(w):
    result = deque()
    for c in w:
        if c == '(':
            result.append(')')
        else:
            result.append('(')
    return result


def loop(w, w_bracket_count):
    if not w:
        return deque([''])
    u_bracket_count = {'(': 0, ')': 0}
    u = deque()
    while w:
        c = w.popleft()
        w_bracket_count[c] -= 1
        u.append(c)
        u_bracket_count[c] += 1
        if w_bracket_count.get('(') == w_bracket_count.get(')'):
            break
    if is_correct(u):
        u.extend(loop(w, w_bracket_count))
        return u
    else:
        result = deque()
        result.append('(')
        result.extend(loop(w, w_bracket_count))
        result.append(')')
        u.popleft()
        u.pop()
        u = reverse_bracket(u)
        result.extend(u)
        return result


def solution(p):
    p = deque(p)
    p_size = len(p) // 2
    p_bracket_count = {'(': p_size, ')': p_size}
    answer = loop(p, p_bracket_count)
    return ''.join(answer)
