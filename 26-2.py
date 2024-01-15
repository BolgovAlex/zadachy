f = open('26-2.txt')
k, w = map(int, f.readline().split())
day = [0] * (w + 1)
for i in range(k):
    start, end = map(int, f.readline().split())
    day[start] += 1
    day[end] -= 1
max_duration, duration, temp_dur = 0, 0, 0
balance = 0
for i in range(w):
    balance += day[i]
    if balance == 0:
        temp_dur += 1
    else:
        max_duration = max(temp_dur, max_duration)
        duration += temp_dur
        temp_dur = 0
print(duration, max_duration)
