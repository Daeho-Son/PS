char = input()
for number in range(0, 26):
    print(char.find(chr(number+97)), end=' ')

# find는 없으면 -1출력, index는 없으면 오류 발생 
# char = input()
# list_count = list(-1 for i in range(26)) # index용1
# for number in range(0, 26):
#     try:  # index용2
#         list_count[number] = char.index(chr(number+97))
#     except ValueError: # index용3
#         pass # index용4
# print(" ".join(map(str, list_count))) # index용5