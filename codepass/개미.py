import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline 


w, h = map(int,input().split())
x, y = map(int,input().split())
t = int(input())


x+= t
y+= t

cntX = x // w 
cntY = y // h

x  = x % w
y  = y % h

if cntX % 2: x = w - x
if cntY % 2: y = h - y

print(x, y)

