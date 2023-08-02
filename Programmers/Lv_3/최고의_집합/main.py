from solution import solution


def main():
    n_list = [
        2,
        2,
        2,
        3,
        3
    ]
    s_list = [
        9,
        1,
        8,
        9,
        10
    ]
    result_list = [
        [4, 5],
        [-1],
        [4, 4],
        [3, 3, 3],
        [3, 3, 4]
    ]

    for _zip, result in zip(zip(n_list, s_list), result_list):
        print('#', *_zip, result)
        if (answer := solution(*_zip)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()
