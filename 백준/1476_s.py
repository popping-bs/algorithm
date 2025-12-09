import sys


sys.stdin = open('input.txt', 'r')

e, s, m = map(int, sys.stdin.readline().split())

year = 1
while True:

    if (year -1) % 15 + 1 == e and \
        (year-1) % 28 + 1 == s and \
        (year-1) % 19 + 1 == m:
        print(year)
        break
    year += 1



#15 - 15,15,15
#16 - 1,16,16 
#17 - 2,17,17
#19 - 3,18,18
#20 - 4,19,19
#21 - 5,20,1
#22 - 6,21,2
#23 - 7,22,3
#24 - 8,23,4

#29 - 14,1,10.  바뀌는 기준이 1이 될 때 나머지랑 차이남.