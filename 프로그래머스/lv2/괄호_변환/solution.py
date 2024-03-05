
# 시도 2. (성공) 다른 사람 풀이를 이해하고 작성 - 2
def solution_2(p):
    bracket_balance = 0
    is_correct_bracket = False
    for i, c in enumerate(p):
        if c == '(':
            bracket_balance += 1
        else:
            bracket_balance -= 1
        if bracket_balance > 0:
            is_correct_bracket = True
        if bracket_balance == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            if is_correct_bracket:
                return u + solution_2(v)
            else:
                return '(' + solution_2(v) + ')' + ''.join(map(lambda x: '(' if x == ')' else ')', u[1:-1]))
    return p


'''
# 시도 1: (실패) 다른 사람 풀이를 이해하고 작성 - 1
## 예외 케이스 1: ))())(((
    - 정답: ()()(())
    - 내 코드: ()(())()
    
## 예외 케이스 2: )))(()((
    - 정답: ()(())()
    - 내 코드: ()()(())
'''
def solution_1(p):
    bracket_balance = 0
    is_correct_bracket = True
    for i, c in enumerate(p):
        if c == '(':
            bracket_balance -= 1
        else:
            bracket_balance += 1
        if bracket_balance > 0:
            is_correct_bracket = False
        if bracket_balance == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            if is_correct_bracket:
                return u + solution_1(v)
            else:
                return '(' + solution_1(v) + ')' + u[i - 1:0:-1]
    return ''

# # 시도 1.
# from collections import deque
#
#
# def is_correct(u):
#     stack = []
#
#     for c in u:
#         if stack and stack[-1] == '(' and c == ')':
#             stack.pop()
#             continue
#         stack.append(c)
#     if stack:
#         return False
#     return True
#
#
# def reverse_bracket(w):
#     result = deque()
#     for c in w:
#         if c == '(':
#             result.append(')')
#         else:
#             result.append('(')
#     return result
#
#
# def loop(w, w_bracket_count):
#     if not w:
#         return deque([''])
#     u_bracket_count = {'(': 0, ')': 0}
#     u = deque()
#     while w:
#         c = w.popleft()
#         w_bracket_count[c] -= 1
#         u.append(c)
#         u_bracket_count[c] += 1
#         if w_bracket_count.get('(') == w_bracket_count.get(')'):
#             break
#     if is_correct(u):
#         u.extend(loop(w, w_bracket_count))
#         return u
#     else:
#         result = deque()
#         result.append('(')
#         result.extend(loop(w, w_bracket_count))
#         result.append(')')
#         u.popleft()
#         u.pop()
#         u = reverse_bracket(u)
#         result.extend(u)
#         return result
#
#
# def solution(p):
#     p = deque(p)
#     p_size = len(p) // 2
#     p_bracket_count = {'(': p_size, ')': p_size}
#     answer = loop(p, p_bracket_count)
#     return ''.join(answer)
