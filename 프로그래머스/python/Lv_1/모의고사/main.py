from solution import solution


def main():
    answers_list = [
        [1, 2, 3, 4, 5],
        [1, 3, 2, 4, 2],
    ]
    return_list = [
        [1],
        [1, 2, 3],
    ]

    for _answers, _return in zip(answers_list, return_list):
        print('#', _answers, _return)
        if (result := solution(_answers)) == _return:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()
