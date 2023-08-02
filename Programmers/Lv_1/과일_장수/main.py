from solution import solution


def main():
    k_list = [3, 4]
    m_list = [4, 3]
    score_list = [[1, 2, 3, 1, 2, 3, 1], [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]]
    answer_list = [8, 33]

    for k, m, score, answer in zip(k_list, m_list, score_list, answer_list):
        print('#', k, m, score, answer)
        if (result := solution(k, m, score)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()
