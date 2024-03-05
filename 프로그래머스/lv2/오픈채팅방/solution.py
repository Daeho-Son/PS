def solution(records):
    message_list = list()
    user_data = dict()
    for record in records:
        r = record.split()
        status = r[0]
        uid = r[1]
        if len(r) == 3:
            nickname = r[2]
            user_data[uid] = nickname
        if status == 'Enter':
            message_list.append((uid, "님이 들어왔습니다."))
        elif status == 'Leave':
            message_list.append((uid, "님이 나갔습니다."))
    answer = list()
    for ml in message_list:
        uid = ml[0]
        message = ml[1]
        answer.append(user_data[uid] + message)
    return answer
