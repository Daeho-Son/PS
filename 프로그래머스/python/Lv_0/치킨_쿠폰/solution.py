def solution(chicken):
    answer = 0
    coupon = 0
    while chicken:
        coupon += chicken
        chicken = coupon // 10
        answer += chicken
        coupon %= 10
    return answer