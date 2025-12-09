import sys

sys.stdin = open("input.txt", 'r')


text = sys.stdin.readline()

n = len(text)

res = ""
for i in range(n):
    res += text[i] #새로 붙여나가는 방식으로 진행.
    if (i+1) % 10 == 0:
        res += "\n"

print(res)
