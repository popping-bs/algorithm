import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split(','))
    print(a+b)