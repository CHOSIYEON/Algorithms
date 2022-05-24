def solution(files):
    answer = []
    newFiles = {}

    for i in range(len(files)):
        alpha = ''
        digit = ''
        tail = False
        for j in range(len(files[i])):
            if files[i][j].isalpha() or files[i][j] in [' ', '.', '-']:
                if not tail:
                    alpha += files[i][j]
                else:
                    break
            elif files[i][j].isdigit():
                digit += files[i][j]
                tail = True
        newFiles[files[i]] = [alpha.lower(), int(digit), i]

    newFiles = dict(sorted(newFiles.items(), key=lambda x: (x[1][0], x[1][1], x[1][2])))

    return list(newFiles.keys())