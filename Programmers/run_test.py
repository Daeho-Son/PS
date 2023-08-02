def run_test(test_case, solution):
    for i, tc in enumerate(test_case):
        _input = tc[:-1]
        _result = tc[-1]
        print(f'### Test Case {i+1} ###')
        print("Input:", *_input)
        print("Result:", _result)
        if (answer := solution(*_input)) == _result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()