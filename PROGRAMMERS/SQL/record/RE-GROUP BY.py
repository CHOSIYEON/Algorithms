# 고양이와 개는 몇 마리 있을까
#
# SELECT animal_type, count(*)
# from animal_ins
# group by animal_type
#
# 동명 동물 수 찾기
#
# SELECT name, count(name)
# from animal_ins
# where name is not NULL
# group by name
# having count(name) >= 2
# order by name
#
# 입양 시각 구하기(1)
#
# SELECT hour(datetime) as hour, count(datetime)
# from animal_outs
# where hour(datetime) >= 9 and hour(datetime) <= 19
# group by hour
# order by hour