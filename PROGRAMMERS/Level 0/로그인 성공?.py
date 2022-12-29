def solution(id_pw, db):
    db = dict(db)

    if id_pw[0] in db.keys():
        if db[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"

    return "fail"