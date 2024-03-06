"""
학회원 입장 여부 확인 (is_enter)
  - 시작한 시간 이전에 대화 한 적이 있는 학회원
  - 개강총회를 시작하자마자 채팅 기록을 남긴 학회원

학회원 퇴장 여부 확인 (is_exit)
  - 개강총회가 끝나고 스트리밍이 끝날 때까지 대화를 한 적이 있는 학회원
    - 개강총회가 끝나자마자 채팅 기록을 남긴 학회원
    - 개강총회 스트리밍이 끝나자마자 채팅 기록을 남긴 학회원

if 개강총회 스트리밍이 끝난 시간 이후:
    다른 스트리밍 영상의 채팅 기록
"""

'''
# 시도 3. (성공) 다른 사람 풀이를 분석하고 구현
## 방법
  1. 입장 시간에 채팅이 있는 username을 entry_users에 추가
  2. 퇴장 시간에 채팅이 있는 username을 exit_users에 추가
  3. 입장과 퇴장 둘 다 있는 학회원의 개수를 반환. len(entry_users & exit_users)

## 실패 원인 분석
  - input = sys.stdin.readline 를 추가 해야 함. 중요
  - set 대신 list로 구현할 경우, 시간 초과
    - dict로 비슷하게 구현 가능. 시간 복잡도가 set과 같은 O(1)
'''
import sys
input = sys.stdin.readline

def time_to_minutes(time):
    return int(time[:2]) * 60 + int(time[3:])


def solution():
    answer = 0
    s, e, q = map(lambda x: time_to_minutes(x), input().split())
    entry_users = set()
    exit_users = set()
    while True:
        try:
            chat_log = input()
            chat_minutes = time_to_minutes(chat_log[:5])
            username = chat_log[6:]
            if 0 <= chat_minutes <= s:
                entry_users.add(username)
            if entry_users and e <= chat_minutes <= q:
                exit_users.add(username)
        except:
            break
    return len(entry_users & exit_users)


if __name__ == '__main__':
    print(solution())


# '''
# # 시도 2. (실패) 시간 초과
# ## 방법
#   1. 입력 받으면서 dict에 username이 존재하지 않으면 0으로 초기화
#   2. 입장 했으면 +1
#   3. 퇴장 했으면 +1
#   4. value가 2인 username의 개수 반환
#
# ## 실패 원인
#   - 입장을 하지 않아도 퇴장 시간에 채팅 두 번을 쓰면 2가 되서 입장했다고 판단됨
# '''
# import sys
# input = sys.stdin.readline
#
# def time_to_minutes(time):
#     hours, minutes = map(int, time.split(':'))
#     return hours * 60 + minutes
#
#
# def solution():
#     answer = 0
#     s, e, q = map(lambda x: time_to_minutes(x), input().split())
#     user_chat_log = {}
#     while True:
#         try:
#             chat_time, username = input().split()
#             chat_minutes = time_to_minutes(chat_time)
#             user_chat_log.setdefault(username, 0)
#             if 0 <= chat_minutes <= s:
#                 user_chat_log[username] += 1
#             if e <= chat_minutes <= q:
#                 user_chat_log[username] += 1
#         except:
#             break
#     return list(user_chat_log.values()).count(2)
#
#
# if __name__ == '__main__':
#     print(solution())

# '''
# # 시도 1. (실패) 시간 초과
# ## 방법
#   1. 입력 받으면서 dict에 채팅 시간 추가. key: 학회원, value: 채팅 시간(list)
#   2. 각 유저의 채팅 시간을 순회하면서 입장했는 지, 퇴장했는 지 체크
# '''
#
# def time_to_minutes(time):
#     hours, minutes = map(int, time.split(':'))
#     return hours * 60 + minutes
#
#
# def solution():
#     answer = 0
#     s, e, q = map(lambda x: time_to_minutes(x), input().split())
#     user_chat_log = {}
#     while True:
#         try:
#             chat_time, username = input().split()
#             user_chat_log.setdefault(username, []).append(time_to_minutes(chat_time))
#         except:
#             break
#     for username, chat_time_log in user_chat_log.items():
#         is_entry = False
#         is_exit = False
#         for chat_time in chat_time_log:
#             if 0 <= chat_time <= s:
#                 is_entry = True
#             if e <= chat_time <= q:
#                 is_exit = True
#         if is_entry and is_exit:
#             answer += 1
#     return answer
#
#
# if __name__ == '__main__':
#     print(solution())
