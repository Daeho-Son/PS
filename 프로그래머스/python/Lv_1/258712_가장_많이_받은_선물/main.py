from run_test import run_test
from solution import solution


def main():
    test_case = [
        # friends	gifts	result
        [["muzi", "ryan", "frodo", "neo"],
         ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"],
         2],
        [["joy", "brad", "alessandro", "conan", "david"],
         ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"], 4],
        [["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"], 0],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
