import time

# time() returns seconds since the Epoch, which is January 1, 1970 on UNIX systems

secs_1day = 24 * 60 * 60
secs_1hour = 60 * 60
secs_1min = 60
print('Seconds, 1 day', secs_1day)
print('Seconds, 1 hour', secs_1hour)
print('Seconds, 1 minute', secs_1min)

# Total seconds
secs_from_epoch = time.time()
print()
print('Seconds from epoch:', secs_from_epoch)

# Days from epoch
day_part_from_epoch = int(secs_from_epoch // secs_1day)
print('Days from epoch:', day_part_from_epoch)

# Hour part from epoch
secs_day_remainder = secs_from_epoch % secs_1day
hour_part_from_epoch = int(secs_day_remainder // secs_1hour)
print()
print('Seconds remainder after days:', secs_day_remainder)
print('Hour part from epoch:', hour_part_from_epoch)

# Minute part from epoch
secs_hour_remainder = secs_day_remainder % secs_1hour
min_part_from_epoch = int(secs_hour_remainder // secs_1min)
print()
print('Seconds remainder after hours:', secs_hour_remainder)
print('Minute part from epoch:', min_part_from_epoch)

# Seconds for today
secs_min_remainder = int(secs_hour_remainder % secs_1min)
print()
print('Seconds remainder after minutes:', secs_min_remainder)

# print('Check (secs in a day * days) + secs today):', (secs_1day * (secs_from_epoch // secs_1day)) + (secs_from_epoch % secs_1day))

# Format time
print()
tm = str(hour_part_from_epoch)+' hours '+str(min_part_from_epoch)+' minutes '+str(secs_min_remainder)+' seconds UTC'
print('THE TIME IS ' + tm)
print()

# Exercise 5
import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

jai = turtle.Turtle()
type(jai)
draw(jai, 10, 10)

turtle.mainloop()
