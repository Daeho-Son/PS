from solution import solution


def main():
    operations_list = [
        ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],
        ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    ]
    return_list = [
        [0, 0],
        [333, -45]
    ]

    for _operations, _return in zip(operations_list, return_list):
        print('#', _operations, _return)
        if (answer := solution(_operations)) == _return:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()