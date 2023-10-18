def is_balanced(s):
    stack = list()
    for c in s:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
        elif stack and stack[-1] == '[' and c == ']':
            stack.pop()
        elif c == '(' or c == ')' or c == '[' or c == ']':
            stack.append(c)
    return False if stack else True


while True:
    if (s := input()) == '.':
        break
    print("yes" if is_balanced(s) else "no")
