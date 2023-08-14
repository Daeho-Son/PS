from run_test import run_test
from solution import solution


def main():
    test_case = [
        # babbling	result
        [["aya", "yee", "u", "maa"], 1],
        [["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"], 2],
        [["ayaaya", "yeye"], 0],
        [["ayaayaye"], 0],
        [["ayayeaya", "yewooye"], 2],
        [["yeayaye", "wooayawoo"], 2]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
