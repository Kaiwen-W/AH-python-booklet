def storeBikes():
    counter = 0
    name = [""] * 6
    gears = [0] * 6
    type = [""] * 6
    price = [0.0] * 6

    with open("bikes.txt", "r", errors="ignore") as readfile:
        line = readfile.readline().rstrip("\n")
        while line:
            items = line.split(",")
            name[counter] = items[0]
            gears[counter] = int(items[1])
            type[counter] = items[2]
            price[counter] = float(items[3])
            line = readfile.readline().rstrip("\n")
            counter += 1

        # print(name, gears, type, price)
    return name, gears, type, price


def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    for i in range(n):
        print(array[i])


def sortParallelArrays(name, gears, type, price):
    n = len(price)

    for i in range(n):
        for j in range(0, n - i - 1):
            if price[j] > price[j + 1]:
                price[j], price[j + 1] = price[j + 1], price[j]

                name[j], name[j + 1] = name[j + 1], name[j]
                gears[j], gears[j + 1] = gears[j + 1], gears[j]
                type[j], type[j + 1] = type[j + 1], type[j]

    for i in range(n):
        print(name[i], gears[i], type[i], price[i])


name, gears, type, price = storeBikes()
sortParallelArrays(name, gears, type, price)
