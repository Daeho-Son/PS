def run_test(test_case, solution):
    total_count = len(test_case)
    answer_count = 0
    wrong_cases = list()
    for i, tc in enumerate(test_case):
        _input = tc[:-1]
        _result = tc[-1]
        print(f'### Test Case {i+1} ###')
        print("Input:", *_input)
        print("Result:", _result)
        if (answer := solution(*_input)) == _result:
            print(answer, "OK")
            answer_count += 1
        else:
            print(answer, "KO")
            wrong_cases.append((i+1, *_input, _result))
        print()
    print(f'테스트 결과 (~˘▾˘)~\n{total_count}개 중 {answer_count}개 성공\n')
    # print(f'# 틀린 테스트 케이스')
    # for case in wrong_cases:
    #     i, _input, _result = case
    #     print(i, _input, _result)
