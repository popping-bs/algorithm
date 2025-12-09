#오른쪽 공백은 런타임 에러 발생할 수 있어!

import sys

sys.stdin = open('input.txt', 'r')


n = int(sys.stdin.readline())

max_line = 2 * n - 1
max_star = 2 * n
for i in range(1, max_line+1):
    if i <= n:
        print("*" * i + " " * (max_star - i * 2)+ "*" * i)
    else:
        print("*" * (2 * n - i)+ " " * ((i-n)*2)+ "*" * (2 * n - i))