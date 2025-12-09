import sys

sys.stdin = open('input.txt', 'r')


n = int(sys.stdin.readline())


for i in range(1, n +1):
    star = '*'

    print(star *(n-i+1) )