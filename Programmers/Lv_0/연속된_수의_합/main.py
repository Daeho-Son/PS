from solution import solution


def main():
    num_list = [
        3,
        5,
        4,
        5,

    ]
    total_list = [
        12,
        15,
        14,
        5
    ]
    result_list = [
        [3, 4, 5],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5],
        [-1, 0, 1, 2, 3],
    ]

    for _zip, result in zip(zip(num_list, total_list), result_list):
        print('#', *_zip, result)
        if (answer := solution(*_zip)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()
