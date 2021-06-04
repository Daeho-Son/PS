def sum_digit(num):
    return sum(map(int, str(num)))

def arrangement(num):
    if num < 10:
        div_m = num    # 기존에 받은 숫자를 반절로 쪼갬
    else:
        div_n, div_m = map(int, str(num))
    sum_n = sum_digit(num)  # 기존에 입력 받은 숫자를 더함
    if sum_n < 10:
        sum_div_n = None
        sum_div_m = sum_n
    else:
        sum_div_n, sum_div_m = map(int, str(sum_n))  # 더한 숫자를 반절로 쪼갬
        
    return div_m*10 + sum_div_m

def count_cycle(num):
    num_clone = num
    count = 0
    while True:
        count += 1
        num_clone = arrangement(num_clone)
        if num == num_clone:
            break
    return count

num = int(input())
if num < 10:
    num = num*10
    count_cycle(num)
    print(count_cycle(num))
else:
    print(count_cycle(num))