list_croatia = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_char = input()
count = 0
for i in list_croatia:
    print(i)
    print(f"input_char.count({i}) = {input_char.count(i)}")
    count += input_char.count(i)
    print(f"count = {count}")
print(len(input_char) - count)

# list_ch = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 
# input_char = input()
# result = 0
# for croatia in list_ch:
#     if croatia in input_char:
#         count = input_char.count(croatia)
#         input_char = input_char.replace(croatia, ',')
#         result += count
#         
# input_char = input_char.replace(',', '')
# print(result + len(input_char))