def solution(chicken):
    answer, coupon = 0, chicken

    while coupon >= 10:
        answer += coupon // 10
        coupon = (coupon // 10) + (coupon - coupon // 10 * 10)

    return answer