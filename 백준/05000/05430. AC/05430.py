"""
# 시도 1.
## 방법
  - 그냥 구현하니까 시간 초과 => 명령어를 압축하는 문제인듯?
"""
import sys

input = sys.stdin.readline


def compress_command_r(command):
    return ''.join(command.split('RR'))


def main():
    t = int(input())  # 테스트 케이스의 개수
    for _ in range(t):
        p = input().rstrip()  # 수행할 함수
        p = compress_command_r(p)
        n = int(input().rstrip())  # 배열에 들어있는 수의 개수
        arr = input().rstrip()[1:-1]
        if arr:
            arr = list(map(int, arr.split(',')))
        else:
            arr = list()
        is_reverse = False
        l_index = 0
        r_index = n
        for i, f in enumerate(p.split('R')):
            if f == '':
                is_reverse = not is_reverse
                continue
            if is_reverse:
                r_index -= len(f)
            else:
                l_index += len(f)
            is_reverse = not is_reverse
        if n - r_index + l_index > n:
            print("error")
            continue
        is_reverse = not is_reverse
        if is_reverse:
            print('[' + ','.join(map(str, arr[l_index:r_index][::-1])) + ']')
        else:
            print('[' + ','.join(map(str, arr[l_index:r_index])) + ']')


if __name__ == '__main__':
    main()
