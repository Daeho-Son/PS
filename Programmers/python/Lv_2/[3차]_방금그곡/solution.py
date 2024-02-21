"""
시도 2. (실패)
- `다른 사람 풀이`를 읽고 다시 작성
- 34번 테스트 케이스 (2024년 2월 21일 추가된 듯)
    - (실패) 소문자가 들어오는 건가 해서 C#, c# 을 1로 치환하는 방식으로 시도

"""


def time_to_minutes(time):
    return int(time[:2]) * 60 + int(time[3:])


def sharp_to_lower(melody):
    sharp_note1 = ['C#', 'D#', 'F#', 'G#', 'A#']
    lower_note = ['c', 'd', 'f', 'g', 'a']
    for sharp, lower in zip(sharp_note1, lower_note):
        melody = melody.replace(sharp, lower)
    return melody


def solution(m, music_infos):
    answer = (-1, '(None)')
    m = sharp_to_lower(m)
    for music_info in music_infos:
        start_time, end_time, title, music_melody = music_info.split(',')
        played_time = time_to_minutes(end_time) - time_to_minutes(start_time)
        music_melody = sharp_to_lower(music_melody)
        div, mod = divmod(played_time, len(music_melody))
        played_melody = music_melody * div + music_melody[:mod]
        if m in played_melody and answer[0] < played_time:
            answer = (played_time, title)
    return answer[-1]


"""
시도 1. (정답)
- `#`을 구분하기 위해 음악 정보를 토큰화한 리스트로 만들고(melody_tokenization), m과 비교하는 과정을 슬라이딩 윈도우 알고리즘으로 풀었다.
- `다른 사람 풀이`를 보면서 토큰화하는 과정, 슬라이딩 윈도우로 비교한 문자를 만드는 과정, heap을 사용해서 재생 시간이 가장 긴 음악을 찾는 과정이 불필요하다고 느꼈다.
"""
# from heapq import heappush, heappop
#
#
# def time_to_minutes(time):
#     hh, mm = map(int, time.split(':'))
#     return hh * 60 + mm
#
#
# def melody_tokenization(melody):
#     melody_token = []
#     for t in melody.split('#'):
#         melody_token += list(t)
#         melody_token[-1] += '#'
#     melody_token[-1] = melody_token[-1][:-1]
#     return melody_token
#
#
# def solution(m, music_infos):
#     answer = []
#     m_size = len(melody_tokenization(m))
#     for s in music_infos:
#         start_time, end_time, title, music_info = s.split(',')
#         music_info = melody_tokenization(music_info)
#         running_time = time_to_minutes(end_time) - time_to_minutes(start_time)
#         div, mod = divmod(running_time, len(music_info))
#         played_melody = music_info * div + music_info[:mod]
#         start_index = 0
#         play = ''.join(played_melody[:m_size])
#         if m == play:
#             heappush(answer, (-running_time, title))
#         for i in range(m_size, len(played_melody)):
#             play = play[len(played_melody[start_index]):] + played_melody[i]
#             start_index += 1
#             if m == play:
#                 heappush(answer, (-running_time, title))
#     if not answer:
#         return "(None)"
#     return heappop(answer)[1]
