from solution import solution


def main():
    numbers_list = [
        [1, 1, 1, 1, 1],
        [4, 1, 2, 1]
    ]
    target_list = [
        3,
        4
    ]
    result_list = [
        5,
        2
    ]

    for numbers, target, result in zip(numbers_list, target_list, result_list):
        print('#', numbers, target, result)
        if (answer := solution(numbers, target)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()