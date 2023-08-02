from solution import solution


def main():
    n_list = [
        10,
        5
    ]
    result_list = [
        4,
        3
    ]

    for n, result in zip(n_list, result_list):
        print('#', n, result)
        if (answer := solution(n)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()