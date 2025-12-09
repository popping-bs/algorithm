import sys

sys.stdin = open("input.txt", "r")


# sys.stdin.readline()

for line in sys.stdin:
    a,b = map(int, line.split())
    print(a+b)