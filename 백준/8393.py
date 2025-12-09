import sys



sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())

total = 0
for i in range(1, n+1):
    total += i

print(total)