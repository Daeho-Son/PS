import time

RED = '\033[31m'
BLUE = '\033[34m'
DEFAULT = '\033[0m'


def run_test(test_case, solution):
    total_count = len(test_case)
    answer_count = 0
    for i, tc in enumerate(test_case):
        start = time.time()
        _input = tc[:-1]
        _result = tc[-1]
        print(f'### Test Case {i + 1} ###')
        print("Input:", *_input)
        print("Result:", _result)
        if (answer := solution(*_input)) == _result:
            print(answer)
            print(BLUE + "통과: ", end='')
            answer_count += 1
        else:
            print(answer)
            print(RED + "실패: ", end='')
        end = time.time()
        print(f"{end - start:.5f} sec" + DEFAULT)
        print()
    print(f'테스트 결과 (~˘▾˘)~\n{total_count}개 중 {answer_count}개 성공\n')
