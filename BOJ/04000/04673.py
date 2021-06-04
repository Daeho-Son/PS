def d():
    set_number = 10000
    self_number = list(i for i in range(1, set_number))
    for number in range(1, set_number):
        jari_sum = 0
        for i in map(int, str(number)):
            jari_sum += i
        try:
            self_number.remove(number + jari_sum)
        except ValueError:
            pass
    return sorted(self_number)

for i in d():
    print(i)