from solution import solution


def main():
    n_list = [
        8, 5, 4, 16
    ]
    m_list = [
        4, 4, 1, 4
    ]
    section_list = [
        [2, 3, 6],
        [1, 3],
        [1, 2, 3, 4],
        [2, 3, 4, 5, 6, 7, 8, 9, 12]
    ]
    result_list = [
        2, 1, 4, 3
    ]

    for inputs, result in zip(zip(n_list, m_list, section_list), result_list):
        print('#', *inputs, result)
        if (answer := solution(*inputs)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()
