import sys

sys.stdin = open('input.txt', 'r')


n = int(sys.stdin.readline())

for i in range(n):
    print(i+1)

