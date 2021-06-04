# 입력된 단어의 알파벳 추출 후 리스트에 저장, 
# 시작 알파벳을 index_alphabet으로 저장해놓고
# 다음 위치부터 입력된 단어의 길이(len(input_char))까지 읽음.
# 만약 단어의 길이가 1일 경우 break, group_check = True
# 만약 알파벳이 바뀌었을 때, 바뀐 위치부터 입력된 단어 끝 부분에
# index_char와 같은 알파벳이 있으면 group_check = False
list_gk = []
list_char = []
for count in range(0, int(input())): # 단어의 개수 N
    list_char.append(list(map(str, input()))) # 단어를 list_char에 append

for input_char in list_char:
    group_check = True
    for alphabet in list(set(input_char)): # 단어의 구성 알파벳을 하나씩 반복
        if len(input_char) == 1: # 단어가 한 글자인 경우 break, group_check = True
            break
        index_alphabet = input_char.index(alphabet)
        for i in range(index_alphabet+1, len(input_char)):
            if input_char[i] != input_char[index_alphabet]:
                if input_char[i:].count(input_char[index_alphabet]) > 0:
                    group_check = False
                    break
                else:
                    break
        if group_check == False:
            break
    if group_check == True:
        list_gk.append(''.join(input_char))
print(len(list_gk))
