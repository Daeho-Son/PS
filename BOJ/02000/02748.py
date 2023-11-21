import time

fibo_count = 0


def fibo(n):
    global fibo_count
    if n == 0 or n == 1:
        return n
    fibo_count += 1
    return fibo(n - 1) + fibo(n - 2)


m = [0] * 51
fibo_top_down_count = 0


def fibo_top_down(n):
    global fibo_top_down_count
    if n == 1 or n == 2:
        return 1
    if m[n] != 0:
        return m[n]
    fibo_top_down_count += 1
    m[n] = fibo_top_down(n - 1) + fibo_top_down(n - 2)
    return m[n]


fibo_bottom_up_count = 0


def fibo_bottom_up(n):
    global fibo_bottom_up_count
    d = [0] * 51
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1):
        d[i] = d[i - 1] + d[i - 2]
        fibo_bottom_up_count += 1
    return d[n]


print("테스트 값 입력:", end=' ')
n = int(input())
print("# fibo 테스트")
start = time.time()
print(f'결과값: {fibo(n)}')
print(f'소요 시간: {time.time() - start:.5f}')
print(f'연산 횟수: {fibo_count}')
print()

start = time.time()
print("# fibo - top down 테스트")
print(f'결과값: {fibo_top_down(n)}')
print(f'소요 시간: {time.time() - start:.5f}')
print(f'연산 횟수: {fibo_top_down_count}')
print()

start = time.time()
print("# fibo - bottom up 테스트")
print(f'결과값: {fibo_bottom_up(n)}')
print(f'소요 시간: {time.time() - start:.5f}')
print(f'연산 횟수: {fibo_bottom_up_count}')
