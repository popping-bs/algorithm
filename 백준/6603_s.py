import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

cases = []
while True:

    line = input().split()
    if not line:
        break
    k = int(line[0])
    if k == 0:
        break
    nums = list(map(int, line[1:]))
    cases.append(nums)

answer = []
def dfs(start,depth,case):

    if depth == 6:
        str_nums = list(map(str,answer))

        print(' '.join(str_nums))

    for i in case:
        if i > start:
            answer.append(i)
            dfs(i,depth+1,case)
            answer.pop()


for case in cases:
    dfs(0,0,case)
    print('')