def run_test(test_case, solution):
    for tc in test_case:
        _input = tc[:-1]
        _result = tc[-1]
        print('#', *_input, _result)
        if (answer := solution(*_input)) == _result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()