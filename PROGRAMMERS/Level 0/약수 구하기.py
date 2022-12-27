def solution(n):
    return [divisor for divisor in range(1, n+1) if not n % divisor]