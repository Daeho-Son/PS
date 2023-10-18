from collections import deque


def solution(input1, input2):
    harmony = deque()
    for a, b in zip(input1, input2):
        harmony.append(int(a))
        harmony.append(int(b))

    while len(harmony) != 2:
        length = len(harmony)-1
        while length:
            print(harmony)
            a = harmony[0]
            b = harmony[1]
            harmony.append((a + b) % 10)
            harmony.popleft()
            length -= 1
        harmony.popleft()
    print(harmony)
    return str(harmony[0]) + str(harmony[1])


def main():
    # a = input()
    # b = input()
    # a = "74759336"
    # b = "36195974"
    a = "01234567"
    b = "12345678"
    result = solution(a, b)
    print(result)


if __name__ == '__main__':
    main()
