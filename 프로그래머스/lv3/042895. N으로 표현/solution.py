"""
# 시도 1 - (성공) 문제 접근을 못 해서 다른 사람 풀이를 이해하고 구현
"""
def solution(N, number):
    combination_by_count = [[()], [(0, 1)]]
    for count in range(2, 9):
        combination_by_count.append([(left, count - left) for left in range(1, count // 2 + 1)])
    dp = [set()]
    all_number = set()
    for i in range(1, 9):
        nn = int(str(N) * i)
        dp.append({nn})
        all_number.add(nn)
        if i < 1:
            continue
        for (left, right) in combination_by_count[i]:
            for d_r in dp[right]:
                for d_l in dp[left]:
                    for calculated_n in [d_r + d_l, d_l - d_r, d_r * d_l, d_r // d_l, d_l // d_r]:
                        if calculated_n < 1 or calculated_n in all_number:
                            continue
                        dp[i].add(calculated_n)
                        all_number.add(calculated_n)
        if number in dp[i]:
            return i
    return -1
