answer = list()


def dfs(numbers, current_index, n):
    if len(numbers) == current_index:
        answer.append(n)
        return
    dfs(numbers, current_index + 1, n + numbers[current_index])
    dfs(numbers, current_index + 1, n - numbers[current_index])


def solution(numbers, target):
    dfs(numbers, 0, 0)
    print(answer)
    return answer.count(target)
