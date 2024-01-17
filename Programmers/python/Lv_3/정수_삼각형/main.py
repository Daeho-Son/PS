from solution import solution


def main():
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    result = 30

    print('#', triangle, result)
    if (answer := solution(triangle)) == result:
        print(answer, "OK")
    else:
        print(answer, "KO")
    print()


if __name__ == '__main__':

    main()