from math import ceil


def get_diff_minutes(out_time, in_time):
    out_time = list(map(int, out_time.split(':')))
    in_time = list(map(int, in_time.split(':')))
    return (out_time[0] * 60 + out_time[1]) - (in_time[0] * 60 + in_time[1])


def solution(fees, records):
    base_minutes, base_fee, credit_minutes, credit_fee = fees
    entrance = dict()
    accumulate_time = dict()
    for record in records:
        time, number, status = record.split()
        if number not in entrance.keys():
            entrance[number] = [time]
        else:
            entrance[number].append(time)
    for k, v in entrance.items():
        if len(entrance[k]) % 2 != 0:
            entrance[k].append("23:59")
        total_minutes = 0
        while v:
            total_minutes += get_diff_minutes(v.pop(), v.pop())
        total_bill = base_fee + ceil((total_minutes - base_minutes) / credit_minutes) * credit_fee
        accumulate_time[k] = total_bill if total_bill >= base_fee else base_fee
    return [a[1] for a in sorted(accumulate_time.items(), key=lambda x: x[0])]
