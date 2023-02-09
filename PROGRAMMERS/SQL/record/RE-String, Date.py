# 루시와 엘라 찾기
#
# SELECT animal_id, name, sex_upon_intake
# from animal_ins
# where name = 'Lucy' or name = 'Ella' or name = 'Pickle' or name = 'Rogan' or name = 'Sabrina' or name = 'Mitty'
# order by animal_id
#
# 이름에 el이 들어가는 동물 찾기
#
# SELECT animal_id, name
# from animal_ins
# where name like '%el%' and animal_type = "dog"
# order by name
#
# 중성화 여부 파악하기
#
# select animal_id, name, if(sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%', 'O', 'X') as 중성화
# from animal_ins
# order by animal_id
#
# 오랜 기간 보호한 동물(2)
#
# SELECT animal_ins.animal_id, animal_ins.name
# from animal_ins inner join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# order by animal_outs.datetime - animal_ins.datetime desc
# limit 2
#
# DATETIME에서 DATE로 형 변환
#
# SELECT animal_id, name, substring(datetime,1,10) as 날짜
# from animal_ins
# order by animal_id