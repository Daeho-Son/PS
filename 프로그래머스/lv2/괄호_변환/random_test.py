import random

from solution import solution_1
from solution import solution_2


def main():
    bracket_count = 4
    p = []
    for i in range(bracket_count):
        p.append('(')
        p.append(')')
    for _ in range(100):
        random.shuffle(p)
        original = ''.join(p)
        if (fail := solution_1(original)) != (success := solution_2(original)):
            print(original)
            print(fail)
            print(success)
            print("KO")
            print()


if __name__ == '__main__':
    main()
