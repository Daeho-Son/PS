from solution import solution


def main():
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    result = 3

    print('#', k, dungeons, result)
    if (answer := solution(k, dungeons)) == result:
        print(answer, "OK")
    else:
        print(answer, "KO")



if __name__ == '__main__':
    main()