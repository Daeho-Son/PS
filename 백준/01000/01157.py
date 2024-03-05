char = input().lower()
list_count = []
for i in range(0, 26):
    list_count.append(char.count(chr(i+97)))
#if list_count.count(max(list_count)) > 1:
#    print("?")
#else:
#    print(chr(list_count.index(max(list_count))+65))
print("?" if list_count.count(max(list_count))>1 else chr(list_count.index(max(list_count))+65))


## count함수 o ##
# input_char = input().lower()
# max_count = -1
# max_char = ''
# for i in range(0, 26):
#     count = input_char.count(chr(i+97))
#     if count == 0:
#         pass
#     elif max_count < count:
#         max_count = count
#         max_char = chr(i+97)
#     elif max_count == count:
#         max_char = '?'
# print(max_char.upper())


## count 함수 x ##
# input_char = input().lower()
# kind_char = set(input_char)
# max_number = 0
# max_char = ''
# for check in kind_char:
#     count = 0
#     for char in input_char:
#         if check == char:
#             count +=1
#     if max_number < count:
#         max_number = count
#         max_char = check
#     elif max_number == count:
#         max_char = '?'
# print(max_char.upper())