number = int(input())

count_5kg, remainder_5kg = divmod(number, 5)
count = -1
for i in range(0, count_5kg+1):
    number_5kg = remainder_5kg + 5*i
    if number_5kg == 0:
        count = count_5kg
        break
    else:
        count_5kg = i
        count_3kg, remainder_3kg = divmod(number_5kg, 3)
        for j in range(0, count_3kg+1):
            number_3kg = remainder_3kg + 3*j
            if number_3kg == 0:
                count = count_5kg + count_3kg
                break
    if count != -1:
        break

    
print(count)