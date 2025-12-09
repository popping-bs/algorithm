import sys


sys.stdin = open('input.txt' , 'r')

n = int(sys.stdin.readline())

number = sys.stdin.readline().strip() #개행문자 지워야함


num_int_list = list(map(int,number))


total = 0
for i in num_int_list:
    total += i
print(total)