from run_test import run_test
from solution import solution


def main():
    test_case = [
        [[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]], 2],
        # [[['a', 1, 'aaa', 'c', 'ng'], ['b', 1, 'bbb', 'c', 'g'], ['c', 1, 'aaa', 'd', 'ng'],
        #   ['d', 2, 'bbb', 'd', 'ng']], 3],
        # [[["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"],
        #   ["d", "2", "bbb", "d", "ng"]], 5]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
