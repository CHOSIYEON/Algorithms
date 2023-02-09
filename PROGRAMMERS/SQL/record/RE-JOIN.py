# 없어진 기록 찾기
#
# SELECT animal_outs.animal_id, animal_outs.name
# from animal_ins right join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# where animal_ins.animal_id is NULL
#
# 있었는데요 없었습니다
# # 날짜가 빠른게 작은거
#
# SELECT animal_ins.animal_id, animal_ins.name
# from animal_ins inner join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# where animal_ins.datetime > animal_outs.datetime
# order by animal_ins.datetime
#
# 오랜 기간 보호한 동물(1)
#
# SELECT animal_ins.name, animal_ins.datetime
# from animal_ins left join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# where animal_outs.animal_id is NULL
# order by animal_ins.datetime
# limit 3
#
# 보호소에서 중성화한 동물
#
# SELECT animal_ins.animal_id, animal_ins.animal_type, animal_ins.name
# from animal_ins inner join animal_outs
# on animal_ins.animal_id = animal_outs.animal_id
# where animal_ins.sex_upon_intake like '%Intact%' and (animal_outs.sex_upon_outcome like '%Spayed%' or animal_outs.sex_upon_outcome like '%Neutered%')
# order by animal_ins.animal_id