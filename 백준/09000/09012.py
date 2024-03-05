def is_vps(ps):
    stack = list()
    for s in ps:
        if stack and stack[-1] == '(' and s == ')':
            stack.pop()
        else:
            stack.append(s)
    return False if len(stack) else True


t = int(input())
for _ in range(t):
    input_s = input()
    print("YES" if is_vps(input_s) else "NO")
