# 투 포인터
# 1. 정렬
# 2. start_index: 0, end_index는 입력 받은 고유 재료의 마지막 인덱스
# 3. start_index에 있는 재료와 end_index에 있는 재료의 합을 비교한다.
def main():
    n = int(input())
    m = int(input())
    ns = sorted(map(int, input().split()))
    answer = 0
    start_index = 0
    end_index = len(ns) - 1
    while start_index < end_index:
        if ns[start_index] + ns[end_index] == m:
            answer += 1
            start_index += 1
            end_index -= 1
        elif ns[start_index] + ns[end_index] < m:
            start_index += 1
        elif ns[start_index] + ns[end_index] > m:
            end_index -= 1
    print(answer)


if __name__ == '__main__':
    main()
