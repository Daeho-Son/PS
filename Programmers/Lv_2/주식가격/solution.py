# def solution(prices):
#     answer = [0] * len(prices)
#     for i, price in enumerate(prices):
#         for t_i in range(i+1, len(prices)):
#             target_price = prices[t_i]
#             answer[i] += 1
#             if price > target_price:
#                 break
#     return answer


def solution(prices):
    answer = [0] * len(prices)
    stack = list()
    for i, price in enumerate(prices):
        while stack:
            target_index, target_price = stack[-1]
            if target_price <= price:
                break
            answer[target_index] = i - target_index
            stack.pop()
        stack.append((i, price))

    while stack:
        index, price = stack.pop()
        answer[index] = len(prices) - index - 1
    return answer
