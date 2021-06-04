dic = {
    '2':'ABC',
    '3':'DEF',
    '4':'GHI',
    '5':'JKL',
    '6':'MNO',
    '7':'PQRS',
    '8':'TUV',
    '9':'WXYZ'
}

input_char = input()
result = 0
for char in input_char:
    for index in range(2, 10):
        if char in dic[str(index)]:
            result += index+1
print(result)