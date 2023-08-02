from solution import solution


def main():
    n_list = [
        5,
        4
    ]
    stages_list = [
        [2, 1, 2, 6, 2, 4, 3, 3],
        [4, 4, 4, 4, 4]
    ]
    result_list = [
        [3, 4, 2, 1, 5],
        [4, 1, 2, 3]
    ]

    for n, stages, result in zip(n_list, stages_list, result_list):
        print('#', n, stages, result)
        if (answer := solution(n, stages)) == result:
            print(answer, "OK")
        else:
            print(answer, "Ko")
        print()


if __name__ == '__main__':
    main()
