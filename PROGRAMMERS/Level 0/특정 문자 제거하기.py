def solution(my_string, letter):
    return ''.join(list(filter(lambda x: x != letter, my_string)))

###

def solution(my_string, letter):
    return my_string.replace(letter, "")