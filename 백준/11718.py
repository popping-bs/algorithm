import sys

sys.stdin = open('input.txt', 'r')

for line in sys.stdin:
    print(line.strip())

