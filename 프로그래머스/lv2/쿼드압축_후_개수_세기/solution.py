def get_answer(answer, arr):
    half = len(arr) // 2
    binary_set = set()
    for a in arr:
        binary_set.update(set(a))
    if len(binary_set) == 1:
        if 1 in binary_set:
            answer[1] += 1
        else:
            answer[0] += 1
    else:
        for hs in range(0, len(arr), half):
            for ws in range(0, len(arr), half):
                get_answer(answer, [s[ws:ws + half] for s in arr[hs:hs + half]])


def solution(arr):
    answer = [0, 0]
    get_answer(answer, arr)
    return answer
