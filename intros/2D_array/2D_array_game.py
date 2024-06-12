import random

rows = 9
cols = 9


def game(display):
    two_d_array = [[random.randint(0, 9) for j in range(cols)] for i in range(rows)]

    if display:
        for x in two_d_array:
            print(x)

    item00 = two_d_array[0][0]
    item88 = two_d_array[8][8]
    item54 = two_d_array[5][4]

    if item00 > item88 and item00 > item54:
        prize = 50
    else:
        prize = -10
    return prize


total = 0

for i in range(100000):
    prize = game(False)
    total += prize

print(prize)
