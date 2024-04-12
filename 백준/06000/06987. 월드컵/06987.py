"""
# 시도 2. 백트래킹
"""
from itertools import combinations

list_of_matches = []
is_possible_result = False


def solution(prediction_result, game_round):
    global is_possible_result
    if game_round == 15:
        is_possible_result = True
        for country_result in prediction_result:
            if country_result.count(0) != 3:
                is_possible_result = False
                break
        return
    country_1, country_2 = list_of_matches[game_round]
    country_1_predict_result = prediction_result[country_1]
    country_2_predict_result = prediction_result[country_2]
    for x, y in [(0, 2), (1, 1), (2, 0)]:
        country_1_predict_result[x] -= 1
        country_2_predict_result[y] -= 1
        if country_1_predict_result[x] >= 0 and country_2_predict_result[y] >= 0:
            solution(prediction_result, game_round + 1)
        country_1_predict_result[x] += 1
        country_2_predict_result[y] += 1


def main():
    global list_of_matches, is_possible_result
    answer = [-1, -1, -1, -1]
    list_of_matches = list(combinations(range(6), 2))
    for i in range(4):
        is_possible_result = False
        prediction_result_input = list(map(int, input().split()))
        prediction_result = [prediction_result_input[i:i+3] for i in range(0, len(prediction_result_input), 3)]
        solution(prediction_result, 0)
        answer[i] = int(is_possible_result)
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()

# """
# # 시도 1. (실패) 모든 예외 찾기
# ## 방법
#   - 한 나라의 승, 무, 패를 더하면 5
#   - 모든 나라의 승, 무, 패를 더하면 30
#   - 모든 나라의 승 == 모든 나라의 패
#   - 모든 나라의 같은 무의 개수가 각각 2의 배수
#     예를 들어, 무승부를 기준으로 (0, 0, 0, 0, 0, 1) 이면 무승부가 1개인 나라가 1개이므로 불가능함
#     예를 들어, 무승부를 기준으로 (0, 0, 0, 0, 1, 1) 이면 무승부가 1개인 나라가 2개이므로 가능함
#  - 승/패이 5인 나라가 있을 경우, 다른 나라는 5일 수 없음
#
# """
#
# from collections import Counter
# from heapq import heappush, heappop
#
#
# def solution():
#     answer = [1, 1, 1, 1]
#     prediction_count = 4
#     country_count = 6
#     for i in range(prediction_count):
#         f = True
#         result_table_input = ''.join(input().split())
#         wins = []
#         loses = []
#         draws = []
#         total_wins = 0
#         total_draws = 0
#         total_loses = 0
#         total_games = 0
#         for j in range(0, country_count * 3, + 3):
#             win, draw, lose = map(int, result_table_input[j:j + 3])
#             if win + draw + lose > country_count - 1:
#                 answer[i] = 0
#             total_wins += win
#             total_draws += draw
#             total_loses += lose
#             total_games += win + draw + lose
#             heappush(wins, (-win, (j // 3, win)))
#             heappush(loses, (-lose, (j // 3, lose)))
#             draws.append(draw)
#         if total_games != country_count * (country_count - 1):
#             answer[i] = 0
#         if total_wins != total_loses:
#             answer[i] = 0
#         for d in Counter(draws).values():
#             if d % 2 != 0:
#                 answer[i] = 0
#                 break
#         while wins:
#             win_country_index, win = heappop(wins)[1]
#             temp_loses = []
#             while loses:
#                 lose_country_index, lose = heappop(loses)[1]
#                 if win_country_index != lose_country_index and win > 0:
#                     lose -= 1
#                 heappush(temp_loses, (-lose, (lose_country_index, lose)))
#                 win -= 1
#             loses = temp_loses
#         if list(filter(lambda x: x[1][1] != 0, loses)):
#             answer[i] = 0
#     return ' '.join(map(str, answer))
#
#
# def main():
#     print(solution())
#
#
# if __name__ == '__main__':
#     main()
