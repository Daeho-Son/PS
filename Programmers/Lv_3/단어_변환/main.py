from run_test import run_test
from solution import solution


def main():
    test_case = [
        # begin	target	words	return
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 4],
        ["hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0],
        ["coo", "kok", ["hot", "cok", "kok"], 2]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
