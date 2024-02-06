'''
- 투 포인터로 풀었다.
- 합이 k인 부분 수열이 여러 개인 경우, 짧은 수열을 찾아야한다.
    - 큰 값부터 시작하기 위해 맨 뒤에서부터 탐색
- 길이가 짧은 수열이 여러개 있는 경우 가장 앞에 나온 수열
    - 다음 인덱스에 있는 값이 맨 뒤에 있는 값과 같다고 하면 종료하지 않고 다음으로 넘긴다.
'''
def solution(sequence, k):
    total = 0
    sequence_end_index = len(sequence) - 1
    start_index = sequence_end_index
    end_index = sequence_end_index
    for i in range(sequence_end_index, -1, -1):
        total += sequence[i]
        start_index = i
        while total > k:
            total -= sequence[end_index]
            end_index -= 1
        if i > 0 and sequence[end_index] == sequence[i-1]:
            continue
        if total == k:
            break

    return [start_index, end_index]
'''
- 역시 시간 초과
- 파이썬 기준 1초에 2,000만번 연산을 수행한다고 가정하면 무리없이 풀 수 있다.
- 문제에 배열의 최대 길이가 100만이라고 하면 O(NlogN)이내의 알고리즘을 이용해 문제를 풀어야한다.
'''
# def solution(sequence, k):
#     answer = ([], 1000000)
#     sequence_length = len(sequence)
#     for i in range(sequence_length):
#         total = 0
#         count = 0
#         for j in range(i, sequence_length):
#             total += sequence[j]
#             count += 1
#             if total == k and count < answer[1]:
#                 answer = ([i, j], count)
#     return answer[0]
#