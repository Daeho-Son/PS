def hansu_count(input_number):
    hansu = 0
    for number in range(1, input_number+1):
        len_number = len(str(number))
        list_jarisu = list(map(int, str(number)))
        if (len_number == 1) or (len_number == 2):
            hansu += 1
        elif len_number == 3:
            if (list_jarisu[0] - list_jarisu[1]) == (list_jarisu[1] - list_jarisu[2]):
                hansu += 1
        elif len_number == 4:
            if (list_jarisu[0] - list_jarisu[1]) == (list_jarisu[1] - list_jarisu[2]) == (list_jarisu[2] - list_jarisu[3]):
                hansu += 1
    return hansu

print(hansu_count(int(input())))