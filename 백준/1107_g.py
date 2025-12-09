import sys

sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

now_channel = 100

if m >0:
    btn = set(map(int, sys.stdin.readline().split()))

else:
    btn = set()
answer = abs(n-100)

def can_make(ch, btn):

    if ch == 0:
        if 0 in btn:
            return 0
        else:
            return 1
        

    length = 0
    while ch > 0:
        digit = ch % 10
        if digit in btn:
            return 0
        
        length +=1

        ch //= 10

    return length


for ch in range(0,1000001):
    length = can_make(ch, btn)
    if length >0:

        press = length + abs(ch - n)
        
        if press < answer:
            answer = press


print(answer)