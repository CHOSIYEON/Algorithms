def solution(m, musicinfos):
    answer = []
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')

    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        musicinfo[3] = musicinfo[3].replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace(
            'G#', 'L')

        time = (int(musicinfo[1].split(':')[0]) * 60 + int(musicinfo[1].split(':')[1])) - (
                    int(musicinfo[0].split(':')[0]) * 60 + int(musicinfo[0].split(':')[1]))

        music = ''.join(musicinfo[3] * (time // len(musicinfo[3])) + musicinfo[3][:time % len(musicinfo[3])])

        if m in music:
            answer.append((time, musicinfo[2]))

    if len(answer) > 0:
        answer.sort(key=lambda x: -x[0])
        return answer[0][1]

    return "(None)"