#문자열 재정렬

data = input()
result = []
value =0


for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)

    else:
        value += int(x)

result.sort()
#숫자가 하나라도 존재하는 경우 가장 뒤에 삽임
if value != 0:
    result.append(str(value))


print(''.join(result))

