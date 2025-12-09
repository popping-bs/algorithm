import sys

sys.stdin = open('input.txt', 'r')

for line in sys.stdin:
    line.strip() #양쪽 지우기.
    a,b = map(int, line.split())

    if a>0 and b < 10:
        print(a+b)