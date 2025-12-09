import sys

sys.stdin = open("input.txt", 'r')


m, d = map(int, sys.stdin.readline().split())


day_31 = [1,3,5,7,8,10,12]
day_30 = [4,6,9,11]
day_28 = [2]

total_days = 0
for month in range(1, m):
    if month in day_31:
        total_days +=31
    elif month in day_30:
        total_days += 30
    else:
        total_days += 28

total_days +=d

week = ['SUN','MON','TUE','WED','THU','FRI', 'SAT']

ss = total_days % 7

print(week[ss])