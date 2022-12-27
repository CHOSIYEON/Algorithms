def solution(cipher, code):
    return ''.join([value for index, value in enumerate(cipher) if index % code == code - 1])