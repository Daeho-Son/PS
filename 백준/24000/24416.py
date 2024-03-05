# Python3 에서 시간 초과가 발생해서 Pypy3 로 채점

answer_fib = 0
answer_fibonacci = 0


def fib(n):
    global answer_fib
    if n == 1 or n == 2:
        answer_fib += 1
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    n = int(input())
    fib(n)
    print(answer_fib, n - 2)


if __name__ == '__main__':
    main()
