def solution(msg):
    answer = list()
    alphabet_list = [chr(ord('A') + i) for i in range(0, 26)]
    lzw_dict = dict(zip(alphabet_list, list(range(1, 27))))
    last_dict_value = 26

    end = 1
    while True:
        if msg in lzw_dict:
            answer.append(lzw_dict.get(msg))
            break
        w = msg[:end]
        next_w = msg[:end + 1]
        if w in lzw_dict and next_w not in lzw_dict:
            answer.append(lzw_dict.get(w))
            lzw_dict[next_w] = last_dict_value + 1
            last_dict_value += 1
            msg = msg[len(w):]
            end = 1
        else:
            end += 1
    return answer


# def solution(msg):
#     answer = list()
#     alphabet_list = [chr(ord('A') + i) for i in range(0, 26)]
#     last_dict_index = 26
#     lzw_dict = dict(zip(alphabet_list, list(range(1, 27))))
#
#     while msg:
#         if msg in lzw_dict:
#             answer.append(lzw_dict.get(msg))
#             break
#         for end in range(1, len(msg) + 1):
#             w = msg[:end]
#             if w not in lzw_dict:
#                 lzw_dict[w] = last_dict_index + 1
#                 last_dict_index += 1
#                 answer.append(lzw_dict.get(msg[:end-1]))
#                 msg = msg[len(w)-1:]
#                 break
#     return answer
