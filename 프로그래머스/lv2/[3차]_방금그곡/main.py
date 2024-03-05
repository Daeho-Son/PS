from run_test import run_test
from solution import solution


def main():
    test_case = [
        # m musicinfos
        ["ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], "HELLO"],
        ["CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], "FOO"],
        ["ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"], "WORLD"],
        ["ABC", ["12:00,12:14,HELLO,ABCDEF", "13:00,13:05,WORLD,ABCDEF"], "HELLO"],
        ["ABC", ["12:00,12:14,HELLO,AB", "13:00,13:05,WORLD,AB"], "(None)"]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
