# 최댓값 구하기
#
# SELECT datetime as 시간
# from animal_ins
# order by datetime desc
# limit 1
#
# SELECT max(datetime) as 시간
# from animal_ins
#
# 최솟값 구하기
#
# SELECT datetime as 시간
# from animal_ins
# order by datetime asc
# limit 1
#
# SELECT min(datetime) as 시간
# from animal_ins
#
# 동물 수 구하기
#
# SELECT count(*) as count
# from animal_ins
#
# 중복 제거하기
#
# SELECT count(distinct name) as count
# from animal_ins
# where name is not NULL