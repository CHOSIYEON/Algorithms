def solution(n, t, m, timetable):
    timetable = sorted(timetable, reverse=True)
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]

    for i in range(n):
        arriveTime = 540 + i * t
        cnt = 0

        while timetable:
            if timetable[-1] > arriveTime or cnt >= m:
                break

            lastTime = timetable[-1]
            timetable.pop()
            cnt += 1

        if not timetable:
            if cnt < m:
                answer = arriveTime
            else:
                answer = lastTime - 1
            return '%02d:%02d' % (answer // 60, answer % 60)

        if i == n - 1:
            if cnt < m:
                answer = arriveTime
            else:
                answer = lastTime - 1
            return '%02d:%02d' % (answer // 60, answer % 60)
